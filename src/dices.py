##!/usr/bin/python3

# Copyright 2022 Felix Schladt (https://github.com/FelixSchladt)

"""
Dice class
"""

from random import randint

class dice:
     def __init__(self):
         self.value = self.roll()
         self.selected = False

     def roll(self):
         self.value = randint(1, 6)
         return self.value

     def switch(self):
         self.selected = not(self.selected)

def get_dices():
    return [ dice() for i in range(5) ]

def reset_dices(dices):
    for dice in dices:
        dice.selected = False
        dice.roll()

if __name__ == "__main__" :
    dices = get_dices()
    for die in dices:
        print(die.value)
