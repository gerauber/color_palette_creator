#############################
## author: G. Räuber, 2024 ##
#############################

from color_palette_creator.colour_modules import get_palette, get_cmap
from color_palette_creator.get_figures import plot_palette
from color_palette_creator.get_figures import plot_cmaps, save_fig


# Create a palette
palettes = [get_palette(6), get_palette(5), get_palette(40),
            get_palette(6, 'teal', lim_sum=0.2),
            ['#2145b882', '#a6a6a6', '#e67500a3']]

palette_plot = []
for pal in palettes:
    palette_plot.append(plot_palette(pal))

for p, plot in enumerate(palette_plot):
    save_fig(plot, f'color_palette_creator/tests/figures/test_palette_{p}')

# Create a cmap
cmaps = [get_cmap(pal, n_bins=600) for pal in palettes]

cmap_plot = plot_cmaps(cmaps)

save_fig(cmap_plot, 'color_palette_creator/tests/figures/test_cmap')
