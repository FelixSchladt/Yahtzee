#!/usr/bin/python3
# Copyright 2022 FelixSchladt (https://github.com/FelixSchladt)

class InvalidLenght(Exception):
    """
    Exception raised if given variable exceeds lenght
    """

class OutOfBounds(Exception):
    """
    Exception raised if a coordinate is outisde of the coordinate spectrum
    """
