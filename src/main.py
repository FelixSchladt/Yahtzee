from enum import Enum


print("┌───────┐")
print("│ ¤   ¤ │")
print("│   ¤   │")
print("│ ¤   ¤ │")
print("└───────┘")

class Dice(Enum):
    ONE   = 1
    TWO   = 2
    THREE = 3
    FOUR  = 4
    FIVE  = 5
    SIX   = 6


for value in Dice:
    print(value)

