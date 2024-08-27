#############################
## author: G. Räuber, 2024 ##
#############################

import matplotlib.pyplot as plt
import numpy as np
import pickle
from matplotlib.colors import LinearSegmentedColormap


def plot_color_gradients(category, cmap_list, filename=''):
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    nrows = len(cmap_list)
    figh = 0.6 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(f'{category} Colormaps', fontsize=14)

    i = 1
    for ax, name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=name)
        ax.text(-0.01, 0.5, f'Custom map {i}', va='center', ha='right',
                fontsize=10, transform=ax.transAxes)
        i += 1

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    if filename:
        plt.savefig(f"{filename}.pdf", bbox_inches='tight')

    plt.show()
