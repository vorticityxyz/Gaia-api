import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import gaia

# Plot results using matplotlib
def plot_results(shot_record):
    fig = plt.figure(figsize=(15, 15))
    scale = np.max(shot_record) / 25000.
    extent = [0, 1, 1, 0]
    plot = plt.imshow(shot_record, vmin=-scale, vmax=scale, cmap=cm.gray, extent=extent)
    plt.show()

# Generate shot profile
def generate_ricker(nt, freq, dt):
    npt = nt * dt
    t = np.arange(-float(npt)/2, float(npt)/2, dt)
    rick1 = 1000 * (1 - t * t * freq**2 * np.pi**2) * np.exp(-t**2 * np.pi**2 * freq**2)
    rick = np.zeros(nt, dtype=np.float32)
    rick[0: nt - (round(nt/2) - round(1/freq/dt) + 1)] = rick1[round(nt/2) - round(1/freq/dt) + 1: nt];
    return rick


def generate_test_data():
    model_file = "data/model_P_5m.npy"
    marmousi = np.load(model_file)
    marmousi = marmousi[1400:2101, :]

    nz = marmousi.shape[1]
    nx = nz
    ny = 351

    marmousi3d = np.zeros((nx, ny, nz), dtype=np.float32)

    for i in range(ny):
        marmousi3d[:, i, :] = marmousi

    fig = plt.figure(figsize=(15, 15))
    plt.contourf(np.swapaxes(marmousi3d[:, 100, :], 0, 1), 100, cmap="viridis")
    plt.gca().invert_yaxis()
    plt.show()

    # Spacial discretization
    dx = 5
    dy = dx
    dz = dx

    vmax = 4700
    vavg = 2670

    # temporal discretization
    sigma = 0.4
    dt = sigma * dx / 4700

    nt = 2 * int((nz * dz / vavg) / dt)

    # Absorbing boundaries
    pmlw = 50
    pmla = 100

    # Shot parameters
    freq = 10           # Frequency
    xs = round(nx/2)    
    ys = round(ny/2)
    zs = 4

    # Receiver parameters
    xt1 = 54
    xt2 = (nx - 55)
    yt1 = round(ny/2)
    yt2 = round(ny/2)
    zt = 4

    model = np.float32(np.square(marmousi3d))
    shot = generate_ricker(nt, freq, dt)
    shotxyz = np.array([xs, ys, zs], dtype=np.int32)
    recxxyz = np.array([xt1, xt2, yt1, yt2, zt], dtype=np.int32)
    deltas = np.array([dx, dy, dz, dt], dtype=np.float32)
    pml = np.array([pmlw, pmla], dtype=np.int32)

    return model, shot, shotxyz, recxxyz, deltas, pml

if __name__ == '__main__':

    # generate test data
    print("Generating test data.")
    model, shot, shotxyz, recxxyz, deltas, pml = generate_test_data()    

    #Call gaia function
    shot_record = gaia.f28pml(model, shot, shotxyz, recxxyz, deltas, pml)
    
    # Test code
    #np.save("data/shot_record.npy", shot_record)
    #shot_record = np.load("data/shot_record.npy")

    # Plot results
    plot_results(shot_record[:, :, 0])