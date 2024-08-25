# Color Palette Creator

## General comments

When a lot of data needs to be presented on a plot, it's generally advisable to 
change the way the data is presented. But if this is not possible, 
it's best to use clearly distinguishable colors. That's why this tool was created:
`color_palette_creator` is a tool that is used to generate a random palette of colours. 
These palettes can be used in the context of plots, and generally improve their readability.
The colours are generated such that they are visible on a white background, 
and each colour is generated so that it is not too close to any of the others in the set.

A class hierarchy has been established for the sole purpose of making it an exercise. 

This code follows the style convention established in the [PEP8 document](https://peps.python.org/pep-0008/).

Version 1.0.4

## Content

This version contains only a basic generator, available in the `basic_generator` folder

### Basic Generator

The principle is the following: 
* run `python main.py`
* specify the number of colours that you would like to generate
* obtain a plot to see the colours
	* if required, generate as many times as you want another plot (all colour codes are printed on the terminal)
	* if you are satisfied with the colours, save the codes in a `.txt` file, and save the figure in a `.pdf` file


