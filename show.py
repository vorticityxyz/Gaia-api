import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# Plot results using matplotlib
def plot_results(shot_record):
    fig = plt.figure(figsize=(15, 15))
    scale = np.max(shot_record) / 10000.
    extent = [0, 2.8, 2.8, 0]
    plot = plt.imshow(shot_record, vmin=-scale, vmax=scale, cmap=cm.gray, extent=extent)
    plt.xlabel('X position (km)')
    plt.ylabel('Time (s)')
    plt.show()

shot_record = np.load("shot_record.npy")

plot_results(shot_record[:, :, 0])




