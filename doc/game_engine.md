# GameEngine

This file provides the engine for the backend of the game.

# How saving works

Save files can be provided with the following parameter: 
```bash
python main.py -s "file_path"
```

If this parameter is not provided the game will be stored automatically
in the file *./save.json*.

When a game is finished, the save file is discarded of.

# Functions

Since this file has a multitude of functions, they are categorized into groups
and only explained in detail if it is necessary.

## Display functions

These functions serve to display the game and its menus.

- invalid_screen_size(self):
	Is shown when the terminal doesnt fit the minimal size requirement

- win_screen(self):
	Displays the screen when a game is won

- draw_game(self):
	This method displays the default frame of the game.
	View dice, a simple "how-to-play" and the scoreboard.

## Control functions

- getch(self):
	Checks whether the terminal still fits the required dimensions
	and returns the key pressed by the user.

- select_rule(self):
	Enables the player to choose what rule they want to use.
	All rules can be chosen, even if they dont provide any points.
	This follows the rules of the game.
	The same rule cannot be chosen twice with an 
	exception of yahtzee/kniffel.

- end_turn(self):
	Defines how the end of a turn is handled.
	The player gets to select a rule if he can do so.
	This method also checks whether the game has finished and displays the winscreen,
	if it has.

- roll_dice(self):
	Rolls all non-stored dice of the player whos turn it is.

- get_active_player_index(self):
	gets the index of whoever players turn it is.
	This index is required to execute the methods of the correct player 
	in other parts of the file.

- game_over(self):
	This function checks whether a game is over and returns True if it is.
	A game is over once both players have used all their rules each.

- soft_exit(self):
	If the exit key (q) is pressed, 
	the game will ask the player for confirmation
	to exit the game with this method.

## Data handling

These functions handle the data of the game

- \_init_players(self, name_one: str, name_two: str):
	This method creates the player objects required for a new game.
	The player names can be chosen freely.
	The max langth of a players name is 10.

- save_game(self):
	This function will save the games state to a file with json-format.
	If the user does not provide a file path, it will default to ./save.json

- load_game(self):
	Loads a game state from a file.
	Also defaults to ./save.json.
