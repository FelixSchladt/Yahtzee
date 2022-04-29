# Terminal
This file provides a system specific terminal handler.

## Functions
- terminal():
	Returns an object of either type *_posix* or *windows*
	depending on the players OS.

	- \_posix
		The terminal handler for linux based systems.

	- \_windows
		The terminal handler for windows systems.

Both classes have the same function, theyre simple implemented 
differently.

- term_size(self):
	Returns the dimensions of the terminal.
	The Size is meassured in Characters.

- clear():
	Clears the terminal.

- getch():
	Get user input.
	Using this method avoids an enter press 
	for each input, makeing for a smoother gameplay
	experience.	
 
