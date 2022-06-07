
# Yahtzee

A simple simulation of the game 'Yahtzee'.
For additional Information please refer to */doc*.

# How to play

## Select a save file
The save file can be chosen with the following parameter:
```bash
python main.py -s "save_file"
```

If no file is provided, the game defaults to the file *./save.json*.

## Select player names
The players names can be chosen with the following parameters:
```bash
python main.py -1 "player_name_one" -2 "player_name_two"
python main.py --player-one "player_name_one" --player-two "player_name_two"
```

If no name is provided, the names default to *"Player 1, Player 2"*.

## Actually play the game
A simple "how-to-play" is printed in the screen when running the game.

One of the two players in randomly selected to go first.
The player can then choose to roll up to 3 times, or end his turn early if he desires to do so.
While rolling, individual dice can be stored, so they wont be rerolled.

When a player cannot roll anymore, he has to select a category he wants to collect points for.
He then gets these points and the category cannot be selected again.
An exception to this rule is the "yahtzee", as one can roll this perticular constellation multiple times.

The game is saved after every turn.

## Ending the game
The game ends once both players have collected points for each category.
The player with more points wins.

After ending a game the respective save file gets removed.

## Keybinds

| Key | Function |
|-----|----------|
| Numbers 1-5 | Store the dice with the respective number |
| Space | Roll the dice |
| Enter | End a turn early |
| q | Exit the game early -> Will save the game! |
