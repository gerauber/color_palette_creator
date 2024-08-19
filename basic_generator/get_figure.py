#############################
## author: G. Räuber, 2024 ##
#############################

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import os

from get_colours import Colours


class Figures:
    def __init__(self):
        self.fig = mpl.figure.Figure

    def get_plot(self, colours: Colours):
        v = colours.number
        cols = colours.list_cols_rgba
        ## compute the width of the figure, and the text
        wid = 8 + int(v/5) * 8
        text_size = 12 - int(v/5)
        ## figure
        figs = plt.figure(figsize=(wid, 6))
        ax = figs.add_subplot(111)
        currentAxis = plt.gca()
        x1, y1 = 0, 0
        xlen, ylen = 0.3, 1
        for i, col in enumerate(cols):
            xa, ya = x1 + (xlen*i), y1
            currentAxis.add_patch(Rectangle((xa, ya), xlen, ylen,
                                  alpha=col[-1], color=col))
            xb, yb = xlen/2 + (xlen*i), ylen/3
            hexcolour = mpl.colors.rgb2hex(col, keep_alpha=True)
            plt.text(xb, yb,
                     f'RGBA: {col}\nhex: {hexcolour}',
                     backgroundcolor='white', ha='center', va='center',
                     size=text_size, rotation='vertical')
        # set limits
        ax.set_xlim([x1, xa + xlen])
        # hide axes
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        self.fig = figs
        plt.show()
        plt.close()

    def get_fig(self):
        return self.fig

    def save_fig(self, path, name):
        if os.path.exists(f'{path}{name}.pdf'):
            i = 0
            while os.path.exists(f'{path}{name}_{i}.pdf'):
                i += 1
            file_name = f'{path}{name}_{i}.pdf'
        else:
            file_name = f'{path}{name}.pdf'
        self.fig.savefig(file_name, bbox_inches='tight')

    def quest_save_figure(self):
        print("Would you like to save the last figure?")
        choice_save_cols = input("(y/n): ")
        if choice_save_cols != 'y' and choice_save_cols != 'n':
            while choice_save_cols != 'y' and choice_save_cols != 'n':
                choice_save_cols = input("Please enter either 'y' or 'n': ")
        return choice_save_cols

    def quest_path_name(self):
        print("Please enter")
        choice_path = input("file path: ")
        choice_name = input("file name: ")
        return [choice_path, choice_name]

    def quest_path_name_corr(self):
        choice_path, choice_name = self.quest_path_name()
        print("\nIs this correct?")
        print(f"File path: {choice_path}\nFile name: {choice_name}")
        choice_path_name = input("(y/n): ")
        if choice_path_name != 'y' and choice_path_name != 'n':
                while choice_path_name != 'y' and choice_path_name != 'n':
                    choice_path_name = input("Please enter either \
                                              'y' or 'n': ")
        if choice_path_name == 'n':
            self.quest_path_name_corr()
        if choice_path_name == 'y':
            self.save_fig(choice_path, choice_name)

    def print_question(self, choice_path, choice_name):
        choice_save_cols = self.quest_save_figure()
        if choice_save_cols == 'y':
            if [choice_path, choice_name] == [None, None]:
                self.quest_path_name_corr()
            else:
                print("Would you like to use the same path and \
                       name for the figure as for the colours?")
                choice_same = input("(y/n): ")
                if choice_same != 'y' and choice_same != 'n':
                        while choice_same != 'y' and choice_same != 'n':
                            choice_same = input("Please enter either \
                                                 'y' or 'n': ")
                if choice_same == 'y':
                    self.save_fig(choice_path, choice_name)
                if choice_same == 'n':
                    self.quest_path_name_corr()
