import numpy as np
from scipy import ndimage, misc
import matplotlib.pyplot as plt
from matplotlib import cm
import gaia

# Plot results using matplotlib
def plot_results(shot_record):
    fig = plt.figure(figsize=(15, 15))
    scale = np.max(shot_record) / 1.
    extent = [0, 1, 1, 0]
    plot = plt.imshow(shot_record, vmin=-scale, vmax=scale, cmap=cm.gray, extent=extent)
    plt.xlabel('X position (km)')
    plt.ylabel('Time (s)')
    plt.show()

def plot_rtm(update):

    nx = update.shape[0]
    ny = update.shape[1]
    nz = update.shape[2]
    
    xSection = np.swapaxes(update[:, round(ny/2), :], 0, 1)
    image = ndimage.laplace(xSection)

    fig = plt.figure(figsize=(15, 15))
    scale = np.max(image) / 0.5
    #extent = [0, 2, 2, 0]
    #extent = [0, 1, 1, 0]
    plot = plt.imshow(image, vmin=-scale, vmax=scale, cmap=cm.gray)
    plt.xlabel('X position (km)')
    plt.ylabel('Z position (km)')
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
    # Earth model dimensions
    nx = 508
    ny = nx
    nz = nx
    # Spacial discretization
    dx = 2.5
    dy = dx
    dz = dx
    # temporal discretization
    dt = 0.0004
    # number of timesteps
    nt = 2500

    # Absorbing boundaries
    pmlw = 50
    pmla = 100

    # Shot parameters
    freq = 30           # Frequency
    xs = round(nx/2)    
    ys = round(ny/2)
    zs = 4
    
    # Receiver parameters
    xt1 = 104
    xt2 = (nx - 105)
    yt1 = round(ny/2)
    yt2 = round(ny/2)
    zt = 4

    # Earth model velocities
    c1 = 1500
    c2 = 2500

    # Generate earth model
    model = np.full((nx, ny, nz), c1**2, dtype=np.float32)
    model[:, :, 151:] = c2**2

    background = np.full((nx, ny, nz), c1**2, dtype=np.float32)

    shot = generate_ricker(nt, freq, dt)
    shotxyz = np.array([xs, ys, zs], dtype=np.int32)
    recxxyz = np.array([xt1, xt2, yt1, yt2, zt], dtype=np.int32)
    deltas = np.array([dx, dy, dz, dt], dtype=np.float32)
    pml = np.array([pmlw, pmla], dtype=np.int32)

    return model, background, shot, shotxyz, recxxyz, deltas, pml

if __name__ == '__main__':

    # generate test data
    print("Generating test data.")
    model, background, shot, shotxyz, recxxyz, deltas, pml = generate_test_data()

    # Call gaia function
    #shot_record = gaia.f28pml(model, shot, shotxyz, recxxyz, deltas, pml)
    shot_record = np.load("data/shot_record.npy")

    forward_record = gaia.f28pml(background, shot, shotxyz, recxxyz, deltas, pml)

    res = shot_record - forward_record

    gradient = gaia.rtm28pml(background, shot, res, shotxyz, recxxyz, deltas, pml)
    np.save("data/gradient.npy", gradient)

    gardient = np.load("data/gradient.npy")
    plot_rtm(gradient)