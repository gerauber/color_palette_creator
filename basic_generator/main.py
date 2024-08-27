#############################
## author: G. Räuber, 2024 ##
#############################

from get_colours import Colours
from get_figure import Figures


def main():
    # number of colours
    print("How many colours would you like?")
    choice_num = int(input("Enter your choice: "))

    cont = True
    while cont:
        # colours
        col = Colours(choice_num)
        col.get_palette()
        col.get_print()

        # plot
        fi = Figures()
        fi.get_plot(col)

        # another try
        print("Another try?")
        ans = input("(y/n): ")
        if ans != 'y' and ans != 'n':
            while ans != 'y' and ans != 'n':
                ans = input("Please enter either 'y' or 'n': ")
        cont = (ans == 'y')

    # save colours
    choice_path, choice_name = col.print_question()

    # save figures
    fi.print_question(choice_path, choice_name)


if __name__ == "__main__":
    main()
