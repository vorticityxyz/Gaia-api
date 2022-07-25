# Description:
# 
# This example uses Vorticity gaia API's mf28pml operator to run a forward model. 
# The operator takes a velocity model and returns a simulated shot record which 
# is then plotted using matplotlib.
#
# Unlike f28pml which runs on a single accelerator card, mf28pml runs on 2 cards
# which allows for larger velocity models.
# 
# Input parameters for the operator is generated by the 
# function generate_test_data() and is as follows:
#
# model - 3D numpy array representing the velocity model
# shot - 1D numpy array representing the shot profile spanning the all timesteps
# shotxyz - Cartesian coordinates of the shot location
# recxxyyz - Cartesian coordinates of the receiver locations
# deltas - dx, dy, dz and dt for the simulation
# pml - width and amplitude of the PML layer
#
# Output: simulated shot record in the form of a 3d numpy array of the format
# shot_record[timestep, x_position, y_position]
# 
# (C) Vorticity Inc. Mountain View, CA 2021
# Licence: MIT

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import gaia

# Plot results using matplotlib
def plot_results(shot_record):
    fig = plt.figure(figsize=(15, 15))
    scale = np.max(shot_record) / 5000.
    extent = [0, 1, 1, 0]
    plot = plt.imshow(shot_record, vmin=-scale, vmax=scale, cmap=cm.gray, extent=extent)
    plt.xlabel('X position')
    plt.ylabel('Time')
    plt.show()

# Generate shot profile
def generate_ricker(nt, freq, dt):
    max_amplitude = 1000
    npt = nt * dt
    t = np.arange(-float(npt)/2, float(npt)/2, dt)
    # generate the short waveform
    rick1 = max_amplitude * (1 - t * t * freq**2 * np.pi**2) * np.exp(-t**2 * np.pi**2 * freq**2)
    # Overlay the short waveform over the full length of timesteps
    rick = np.zeros(nt, dtype=np.float32)
    rick[0: nt - (round(nt/2) - round(1/freq/dt) + 1)] = rick1[round(nt/2) - round(1/freq/dt) + 1: nt];
    return rick

def generate_test_data():
    # Earth model dimensions
    nx = 1001
    ny = 1001
    nz = 1601

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

    # Build earth model
    model = np.full((nx, ny, nz), c1, dtype=np.float32)      # Smooth model
    model[:, :, 151:] = c2                                   # Now insert step

    # Generate rest of the parameters
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

    # Call gaia function
    shot_record = gaia.mf28pml(model, shot, shotxyz, recxxyz, deltas, pml)
    
    # Plot results
    plot_results(shot_record[:, :, 0])

    # Save shot record for rtm later
    np.save("data/shot_record", shot_record)