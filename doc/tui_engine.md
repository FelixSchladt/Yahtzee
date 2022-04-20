# Tui Engine

## TuiEngine Class

Class which provides functionality to use the terminal as an interactive display.

This is achieved by representing each character in the terminal as a field in a
2-dimensional array called *grid*.

### pixel()

Base function for assigning a character to the grid.
Raises **OutOfBoundsError** if coordinates are invalid.
All other functions for drawing shapes and text are based upon the pixel function.

### flush()

Flush draws the current state of the grid buffer onto the terminal.
Uses ASCII control sequences to navigate


