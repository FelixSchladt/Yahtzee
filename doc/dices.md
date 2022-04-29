# Dices 

Contains the code required to create and handle dice.

## Dice class

This class represents a single dice.

**Functions**
- roll(self):
	Rolls the dice.
	This will assign a new value between 1 and 6 
	to it.

- switch(self):
	Toggles the dice between *selected* and *not selected*.
	A dice can only be rolled if it is not selected.

## Additional Functions
- get_dices():
	returns 5 objects of type Dice.

- reset_dice(dice: []):
	Deselects all dice in the list 
	and rerolls them.
	This is used between the turns of the two players
	to simulate the first roll.
