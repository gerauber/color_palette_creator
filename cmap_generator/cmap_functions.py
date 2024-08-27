#############################
## author: G. Räuber, 2024 ##
#############################

import pickle
from matplotlib.colors import LinearSegmentedColormap


def custom_colormap(colour_set, cmap_name, n_bins):
    custom_cmap = LinearSegmentedColormap.from_list(cmap_name,
                                                    colour_set,
                                                    N=n_bins)
    return custom_cmap


def save_colors(custom_cmap, output_file):
    pickle.dump(custom_cmap, open(f'{output_file}.pkl', "wb"))


def read_colors(input_file):
    with open(f'{input_file}.pkl', 'rb') as f:
        c_file = pickle.load(f)
    return c_file
