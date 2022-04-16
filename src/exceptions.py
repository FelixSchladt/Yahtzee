#!/usr/bin/python3

# Copyright 2022 Felix Schladt (https://github.com/FelixSchladt)

'''
This module contains some custom exceptions
'''

class InvalidLenghtError(Exception):
    """
    Exception raised if given variable exceeds lenght
    """

class OutOfBoundsError(Exception):
    """
    Exception raised if a coordinate is outisde of the coordinate spectrum
    """
