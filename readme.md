# Color Palette Creator

## General comments

`color_palette_creator` is a tool that is used to generate a random palette of colours. 
These palettes can be used in the context of plots, and generally improve their readability.
The colours are generated such that they are visible on a white background, 
and each colour is generated so that it is not too close to any of the others in the set.

## Content

This version contains only a basic generator, available in the `basic_generator` folder

### Basic Generator

The principle is the following: 
* run `python main.py`
* specify the number of colours that you would like to generate
* obtain a plot to see the colours
	* if required, generate as many times as you want another plot (all colour codes are printed on the terminal)
	* if you are satisfied with the colours, save the codes in a `.txt` file, and save the figure in a `.pdf` file


