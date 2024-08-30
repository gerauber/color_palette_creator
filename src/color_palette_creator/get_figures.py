#############################
## author: G. Räuber, 2024 ##
#############################

import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import os


def plot_palette(list_cols_rgba_hex):
    v = len(list_cols_rgba_hex)
    # Compute the width of the figure, and the text
    wid = 8 + int(v/5) * 8
    text_size = 12 - int(v/5)
    # Figure
    figs = plt.figure(figsize=(wid, 6))
    ax = figs.add_subplot(111)
    currentAxis = plt.gca()
    x1, y1 = 0, 0
    xlen, ylen = 0.3, 1
    for i, col in enumerate(list_cols_rgba_hex):
        xa, ya = x1 + (xlen*i), y1
        xb, yb = xlen/2 + (xlen*i), ylen/3
        if isinstance(col, str):
            rgb_a = 'RGBA'
            col_rgb_a = [float(f'{c:<0.2f}') for c in mpl.colors.to_rgba(col)]
            col_hex = col
            currentAxis.add_patch(Rectangle((xa, ya), xlen, ylen,
                                  alpha=col_rgb_a[-1], color=col_rgb_a))
        elif len(col) == 3:
            rgb_a = 'RGB'
            col_rgb_a = col
            col_hex = mpl.colors.rgb2hex(col)
            currentAxis.add_patch(Rectangle((xa, ya), xlen, ylen,
                                  color=col_rgb_a))
        elif len(col) == 4:
            rgb_a = 'RGBA'
            col_rgb_a = col
            col_hex = mpl.colors.rgb2hex(col, keep_alpha=True)
            currentAxis.add_patch(Rectangle((xa, ya), xlen, ylen,
                                  alpha=col_rgb_a[-1], color=col_rgb_a))

        plt.text(xb, yb,
                 f'{rgb_a}: {col_rgb_a}\nhex: {col_hex}',
                 backgroundcolor='white', ha='center', va='center',
                 size=text_size, rotation='vertical')
    # Set limits
    ax.set_xlim([x1, xa + xlen])
    # Hide axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    plt.close()
    return figs


def plot_cmaps(cmap_list):
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    nrows = len(cmap_list)
    figh = 0.6 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))

    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(f'Colormaps', fontsize=14)

    i = 1
    for ax, name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=name)
        ax.text(-0.01, 0.5, f'Custom map {i}', va='center', ha='right',
                fontsize=10, transform=ax.transAxes)
        i += 1

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    plt.show()
    plt.close()
    return fig


def save_fig(fig, path, name=''):
    file_name = f'{path}{name}.pdf'
    fig.savefig(file_name, bbox_inches='tight')


def save_fig_no_override(fig, path, name=''):
    if os.path.exists(f'{path}{name}.pdf'):
        i = 0
        while os.path.exists(f'{path}{name}_{i}.pdf'):
            i += 1
        file_name = f'{path}{name}_{i}.pdf'
    else:
        file_name = f'{path}{name}.pdf'
    fig.savefig(file_name, bbox_inches='tight')
