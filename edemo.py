import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import gaia
import sys

def plot_etraces(vx_traces, vy_traces, vz_traces):
    fig = plt.figure(figsize=(15, 15))
    scale = np.max(vx_traces) / 500.
    extent = [0, 2, 2, 0]
    #extent = [0, 1, 1, 0]
    plot = plt.imshow(vx_traces, vmin=-scale, vmax=scale, cmap=cm.gray, extent=extent)
    plt.xlabel('X position (km)')
    plt.ylabel('Time (s)')
    plt.show()

    fig = plt.figure(figsize=(15, 15))
    scale = np.max(vy_traces) / 500.
    extent = [0, 2, 2, 0]
    #extent = [0, 1, 1, 0]
    plot = plt.imshow(vy_traces, vmin=-scale, vmax=scale, cmap=cm.gray, extent=extent)
    plt.xlabel('X position (km)')
    plt.ylabel('Time (s)')
    plt.show()

    fig = plt.figure(figsize=(15, 15))
    scale = np.max(vz_traces) / 500.
    extent = [0, 2, 2, 0]
    #extent = [0, 1, 1, 0]
    plot = plt.imshow(vz_traces, vmin=-scale, vmax=scale, cmap=cm.gray, extent=extent)
    plt.xlabel('X position (km)')
    plt.ylabel('Time (s)')
    plt.show()

def generate_ricker(nt, freq, dt):
    npt = nt * dt
    t = np.arange(-float(npt)/2, float(npt)/2, dt)
    rick1 = 1 * (1 - t * t * freq**2 * np.pi**2) * np.exp(-t**2 * np.pi**2 * freq**2)
    rick = np.zeros(nt, dtype=np.float32)
    rick[0: nt - (round(nt/2) - round(1/freq/dt) + 1)] = rick1[round(nt/2) - round(1/freq/dt) + 1: nt];
    return rick

def generate_elastic_data():

    nx = 501
    ny = nx
    nz = nx
    dt = 0.0002 #0.0001333333333

    dx = 1.0
    dy = dx
    dz = dx

    nt = 2000

    freq = 50.0
    xs = round(nx/2)
    ys = round(ny/2)
    zs = 4

    # simulation accuracy
    act = 2       # temporal accuracy
    acs = 8       # spacial accuracy
    # absorbing boundary conditions
    # 0 - none, 1 - pml, 2 - sponge
    abc = 2

    # Absorbing boundary conditions
    # 0 - sine profile
    abcw = 50
    abca = 8        # alpha * 1000

    # Receiver setup
    xt1 = 54
    xt2 = (nx - 55)
    yt1 = round(nx/2)
    yt2 = round(nx/2)
    zt = 4

    # Earth model setup
    c1 = 1500
    c2 = 2000

    # Generate earth model
    vp = np.full((nx, ny, nz), c1**2, dtype=np.float32)
    vs = np.full((nx, ny, nz), (c1/2)**2, dtype=np.float32)
    rho = np.full((nx, ny, nz), 1.0, dtype=np.float32)

    # Add step
    vp[:, :, 151:] = c2**2
    vs[:, :, 151:] = (c2/2)**2

    shot = generate_ricker(nt, freq, dt)
    shotxyz = np.array([xs, ys, zs], dtype=np.int32)
    recxxyyz = np.array([xt1, xt2, yt1, yt2, zt], dtype=np.int32)
    deltas = np.array([dx, dy, dz, dt], dtype=np.float32)
    abc = np.array([abcw, abca], dtype=np.int32)

    return vp, vs, rho, shot, shotxyz, recxxyyz, deltas, abc

if __name__ == '__main__':

    print("Generating elastic test data...")    
    vp, vs, rho, shot, shotxyz, recxxyyz, deltas, abc = generate_elastic_data()

    vx, vy, vz = gaia.ef18abc(vp, vs, rho, shot, shotxyz, recxxyyz, deltas, abc)

    plot_etraces(vx[:, :, 0], vy[:, :, 0], vz[:, :, 0])

    np.savez("data/e_traces.npz", vx=vx, vy=vy, vz=vz)