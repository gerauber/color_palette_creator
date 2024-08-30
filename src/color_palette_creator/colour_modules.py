#############################
## author: G. Räuber, 2024 ##
#############################

import matplotlib as mpl
import os
import numpy as np
import pickle
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import colors
import colorsys
from sys import exit


# Colour palette functions
def rand_col(min_val, max_val):
    value = np.random.uniform(min_val, max_val)
    return float(f'{value:<0.2f}')


def too_close(list_cols, co, lim_sum=0.5):
    for cols in list_cols:
        diff = [abs(cols[i]-co[i]) for i in range(len(cols))]
        if sum(diff) <= lim_sum:
            return True
    return False


def rgba2hex(list_rgba):
    return [mpl.colors.rgb2hex(row, keep_alpha=True) for row in list_rgba]


def get_palette(number, key='',
                lim_s1=0.3, lim_s2=1,
                lim_l1=0.2, lim_l2=0.7,
                lim_rgb1=0, lim_rgb2=0.9,
                lim_a1=0.2, lim_a2=1, lim_sum=0.5, lim_iter=500):
    """
    Create a palette of colours
    Parameters:
    number (int): number of colours
    key (str): a python colour, such as 'blue'
    lim_s1, lim_s2 (floats): Limits of saturation (S),
    for colours in HSL, in [0, 1]
    lim_l1, lim_l2 (floats): Limits of light (L),
    for colours in HSL, in [0, 1]
    lim_rgb1, lim_rgb2 (floats): Limits of red, green and blue (RGB),
    for colours in RGBA, in [0, 1]
    lim_a1, lim_a2 (floats): Limits of alpha (A),
    for colours in RGBA, in [0, 1]
    lim_sum (float): Limit set to avoid similar colours.
    Recommended to be set at 0.5 for RGBA, and 0.3 when a key is given
    lim_iter (int): Limit set to avoid an infinite loop
    Returns:
    list: A set of colours
    """
    if key:
        rgb_base = mpl.colors.to_rgb(key)
        hsl_base = colorsys.rgb_to_hls(rgb_base[0], rgb_base[1], rgb_base[2])
        cols, i, lim = [], 0, 0
        while i < number:
            hsl_mod = [hsl_base[0],
                       rand_col(lim_s1, lim_s2),
                       rand_col(lim_l1, lim_l2)]
            co = colorsys.hls_to_rgb(hsl_mod[0], hsl_mod[1], hsl_mod[2])
            if co not in cols and not too_close(cols, co, lim_sum):
                cols.append([float(f'{c:<0.2f}') for c in co])
                i += 1
            lim += 1
            if lim == lim_iter:
                exit((f'constraints are too tight, \
                     please decrease the number of colours ({number}) \
                     or the contraining term "lim_sum" ({lim_sum})'))
    else:
        cols, i, lim = [], 0, 0
        while i < number:
            co = [rand_col(lim_rgb1, lim_rgb2),
                  rand_col(lim_rgb1, lim_rgb2),
                  rand_col(lim_rgb1, lim_rgb2),
                  rand_col(lim_a1, lim_a2)]
            if co not in cols and not too_close(cols, co, lim_sum):
                cols.append(co)
                i += 1
            lim += 1
            if lim == lim_iter:
                exit(f'constraints are too tight, \
                     please decrease the number of colours ({number}) \
                     or the contraining term "lim_sum" ({lim_sum})')
    return cols


# Colour maps functions
def get_cmap(colour_set, cmap_name='custom_map', n_bins=500):
    """
    Create a colour map
    Parameters:
    colour_set (list): List of colours
    cmap_name (str): Name of Cmap
    n_bins (int): Number of colours in the colour map
    Returns:
    matplotlib.colors.LinearSegmentedColorma: A colour map
    """
    custom_cmap = LinearSegmentedColormap.from_list(cmap_name,
                                                    colour_set,
                                                    N=n_bins)
    return custom_cmap
