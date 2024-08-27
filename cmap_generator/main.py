#############################
## author: G. Räuber, 2024 ##
#############################

from cmap_functions import custom_colormap, save_colors, read_colors
from cmap_visualize import plot_color_gradients

# Create a dictionary with different color palettes
color_set = [[0.84, 0.05, 0.09, 0.63],
             [0.14, 0.41, 0.2, 0.82],
             [0.84, 0.05, 0.61, 0.51],
             [0.09, 0.52, 0.59, 0.21],
             [0.27, 0.26, 0.26, 0.59]]
cmap_name = 'Custom_cmap_1'
n_bins = 5

dict_colours = {}
dict_colours['set_1'] = {}
dict_colours['set_1']['cs'] = color_set
dict_colours['set_1']['cn'] = cmap_name
dict_colours['set_1']['nb'] = n_bins

dict_colours['set_2'] = {}
dict_colours['set_2']['cs'] = ['#2145b882', '#a6a6a6', '#e67500a3']
dict_colours['set_2']['cn'] = 'Custom_cmap_2'
dict_colours['set_2']['nb'] = 300

dict_colours['set_3'] = {}
dict_colours['set_3']['cs'] = [[0.23, 0.83, 0.18, 0.81],
                               [0.33, 0.38, 0.34, 0.68],
                               [0.9, 0.54, 0.24, 0.35],
                               [0.52, 0.65, 0.52, 0.73],
                               [0.75, 0.16, 0.77, 0.26],
                               [0.2, 0.34, 0.66, 0.58],
                               [0.26, 0.08, 0.04, 0.55],
                               [0.07, 0.56, 0.12, 0.88],
                               [0.56, 0.2, 0.26, 0.35],
                               [0.39, 0.58, 0.57, 0.28],
                               [0.09, 0.79, 0.82, 0.38],
                               [0.11, 0.85, 0.31, 0.28],
                               [0.22, 0.76, 0.4, 0.58],
                               [0.84, 0.84, 0.65, 0.68],
                               [0.88, 0.21, 0.1, 0.8],
                               [0.77, 0.3, 0.65, 0.62],
                               [0.03, 0.48, 0.7, 0.93],
                               [0.78, 0.41, 0.13, 0.59],
                               [0.5, 0.58, 0.05, 0.83],
                               [0.53, 0.01, 0.61, 0.72],
                               [0.49, 0.43, 0.36, 0.21],
                               [0.73, 0.85, 0.81, 0.45],
                               [0.16, 0.17, 0.25, 0.28],
                               [0.24, 0.64, 0.07, 0.32],
                               [0.0, 0.25, 0.54, 0.45],
                               [0.35, 0.08, 0.43, 0.46],
                               [0.03, 0.32, 0.88, 0.31],
                               [0.61, 0.26, 0.48, 0.94],
                               [0.02, 0.23, 0.2, 0.71],
                               [0.54, 0.0, 0.15, 0.8],
                               [0.64, 0.73, 0.86, 0.94],
                               [0.67, 0.04, 0.02, 0.51],
                               [0.18, 0.24, 0.6, 0.97],
                               [0.07, 0.78, 0.5, 0.87],
                               [0.69, 0.48, 0.59, 0.43],
                               [0.28, 0.58, 0.37, 0.91],
                               [0.01, 0.35, 0.04, 0.25],
                               [0.83, 0.67, 0.43, 0.21],
                               [0.36, 0.87, 0.72, 0.74],
                               [0.35, 0.24, 0.11, 0.92],
                               [0.73, 0.71, 0.05, 0.31],
                               [0.66, 0.89, 0.21, 0.98],
                               [0.47, 0.56, 0.23, 0.5],
                               [0.37, 0.37, 0.79, 0.94],
                               [0.69, 0.48, 0.73, 0.84],
                               [0.52, 0.77, 0.83, 0.23],
                               [0.88, 0.53, 0.84, 0.33],
                               [0.48, 0.19, 0.87, 0.55],
                               [0.6, 0.06, 0.82, 0.99],
                               [0.07, 0.46, 0.61, 0.21]]
dict_colours['set_3']['cn'] = 'Custom_cmap_3'
dict_colours['set_3']['nb'] = 50

dict_colours['set_4'] = {}
dict_colours['set_4']['cs'] = ['#a8ccd436', '#4cdb3857', '#30bf96b5',
                               '#1c788ad1', '#7a6b0ac2']
dict_colours['set_4']['cn'] = 'Custom_cmap_4'
dict_colours['set_4']['nb'] = 600

# Create the colour maps
cmaps = []
dict_entries = [c for c in dict_colours]
for c in dict_entries:
    cmaps.append(custom_colormap(dict_colours[c]['cs'],
                                 dict_colours[c]['cn'],
                                 dict_colours[c]['nb']))

# Plot the colour maps
plot_color_gradients('Custom', cmaps, 'custom_colormaps')

# Save the colour maps
for i in range(len(cmaps)):
    save_colors(cmaps[i], dict_colours[dict_entries[i]]['cn'])

# If needed, call the one of the created file
# cmap_1 = read_colors(Custom_cmap_1)
