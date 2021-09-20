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

    block = np.load('data/marmousi3d.npy')

    '''nx = block.shape[1]
    ny = block.shape[1]
    nz = block.shape[1]
    marmousi2d = block[:, round(ny/2), :]
    fig = plt.figure(figsize=(48, 10))
    plt.contourf(np.swapaxes(marmousi2d, 0, 1))
    plt.gca().invert_yaxis()
    plt.show()'''

    box_nx = 701
    box_ny = 701
    box_nz = 701

    dx = 5
    dy = dx
    dz = dx

    F = 10
    dt = 0.00043
    nt = 7000

    pmlw = 100
    pmla = 30
    ghost = 4       # ghost points

    xs = round(box_nx/2)
    ys = round(box_ny/2)
    zs = ghost

    xt1 = pmlw + ghost
    xt2 = (box_nx - pmlw - ghost - 1)
    yt1 = round(box_ny/2)
    yt2 = round(box_ny/2)
    zt = ghost

    x_start = 0
    x_end = 2
    x_step = 1

    y_start = 0
    y_end = 0
    y_step = 0

    shotbox = np.array([box_nx, box_ny, box_nz], dtype=np.int32)
    sweep = np.array([x_start, x_end, x_step, y_start, y_end, y_step], dtype=np.int32)
    shot = generate_ricker(nt, F, dt)
    shotxyz = np.array([xs, ys, zs], dtype=np.int32)
    recxxyyz = np.array([xt1, xt2, yt1, yt2, zt], dtype=np.int32)
    deltas = np.array([dx, dy, dz, dt], dtype=np.float32)
    pml = np.array([pmlw, pmla], dtype=np.int32)

    return block, shotbox, sweep, shot, shotxyz, recxxyyz, deltas, pml

if __name__ == '__main__':
    
    print("Generating test data.")
    destination = "results/"
    block, shotbox, sweep, shot, shotxyz, recxxyyz, deltas, pml = generate_batch_data()
    gaia.batchf28pml(block, shotbox, sweep, shot, shotxyz, recxxyyz, deltas, pml, destination)