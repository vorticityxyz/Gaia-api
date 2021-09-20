import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import gaia

# Generate shot profile
def generate_ricker(nt, freq, dt):
    npt = nt * dt
    t = np.arange(-float(npt)/2, float(npt)/2, dt)
    rick1 = 1 * (1 - t * t * freq**2 * np.pi**2) * np.exp(-t**2 * np.pi**2 * freq**2)
    rick = np.zeros(nt, dtype=np.float32)
    rick[0: nt - (round(nt/2) - round(1/freq/dt) + 1)] = rick1[round(nt/2) - round(1/freq/dt) + 1: nt];
    return rick

def generate_batch_data():

    model_nx = 1001
    model_ny = 501
    model_nz = 501

    shotbox_nx = 501
    shotbox_ny = 501
    shotbox_nz = 501

    dx = 5
    dy = dx
    dz = dx

    F = 10
    dt = 0.00043
    nt = 7000

    pmlw = 100
    pmla = 30
    ghost = 4       # ghost points

    xs = round(shotbox_nx/2)
    ys = round(shotbox_ny/2)
    zs = ghost

    xt1 = pmlw + ghost
    xt2 = (shotbox_nx - pmlw - ghost - 1)
    yt1 = round(shotbox_ny/2)
    yt2 = round(shotbox_ny/2)
    zt = ghost

    x_start = 0
    x_end = 2
    x_step = 1

    y_start = 0
    y_end = 0
    y_step = 0

    # Earth model setup
    c1 = 1500**2
    c2 = 2500**2

    # Generate earth model
    model = np.full((model_nx, model_ny, model_nz), c1, dtype=np.float32)
    model[:, :, 151:] = c2

    shotbox = np.array([shotbox_nx, shotbox_ny, shotbox_nz], dtype=np.int32)
    sweep = np.array([x_start, x_end, x_step, y_start, y_end, y_step], dtype=np.int32)
    shot = generate_ricker(nt, F, dt)
    shotxyz = np.array([xs, ys, zs], dtype=np.int32)
    recxxyyz = np.array([xt1, xt2, yt1, yt2, zt], dtype=np.int32)
    deltas = np.array([dx, dy, dz, dt], dtype=np.float32)
    pml = np.array([pmlw, pmla], dtype=np.int32)

    return model, shotbox, sweep, shot, shotxyz, recxxyyz, deltas, pml

if __name__ == '__main__':
    
    print("Generating test data.")
    destination = "results/"
    model, shotbox, sweep, shot, shotxyz, recxxyyz, deltas, pml = generate_batch_data()
    gaia.batchf28pml(model, shotbox, sweep, shot, shotxyz, recxxyyz, deltas, pml, destination)