# General Information

This directory contains the projects documentation.
All source-code goes into the source-directory **"/src"**.

The markdown files in this directory are made to work with githubs markdown syntax.

## Requirements

For running the game, a minimal terminal size is requiered. 
**Please maximize the terminal**. 
Terminal emulators of developement environments like the one built into Pycharm will very likely not work,
as they don't fit the required dimensions.

The minimum requirements are:
- Height: 38 Characters
- Width: 123 Characters 

### For Windows Users

Since this project was developed on Linux,
theres some minimal issues problems when using windows.

The default windows terminal is quite slow when it comes to rendering. 
Some flickering must be excpected. We would recommend the use of a gpu-accalerated terminal such as Kitty or Alacritty,
but if a Windows environment is preferred we would recommend the new win11 terminal or powershell. 

## Pylint errors

There are two unfixable pylint errors in this project.
They will be explained here.

Both originate from src/terminal.py which provides OS specific access to terminal related functionality.

1.  
```bash
src/terminal.py:18:4: E0401: Unable to import 'msvcrt' (import-error)
```
This error is specific to a non Windows environment. The msvcrt module is a built in pyhton module that
provides windows specific functionality.
A similar Error should appear about the Modules "tty" and "termios" on Windows (I can't check this).

2. 
```bash
src/terminal.py:22:0: R0903: Too few public methods (0/2) (too-few-public-methods)
```
The class in question is the Colors class in terminal.py which provides easy access to ASCII colorcodes.
This class is just a wrapper for constants and therefore does not have any functions related to it.
We believe this is the neatest way to bundle these constants and therefore ignored pylint's
requirement.

# Files

Documentation for the source code:
- [tui_engine.md](https://github.com/FelixSchladt/kniffel/blob/main/doc/tui_engine.md)
- [terminal.py](https://github.com/FelixSchladt/kniffel/blob/main/doc/terminal.md)
- [game_engine.md](https://github.com/FelixSchladt/kniffel/blob/main/doc/game_engine.md)
- [file_handler.md](https://github.com/FelixSchladt/kniffel/blob/main/doc/file_handler.md)
- [rules.md](https://github.com/FelixSchladt/kniffel/blob/main/doc/rules.md)
- [dices.md](https://github.com/FelixSchladt/kniffel/blob/main/doc/dices.md)

Additional files:
- played_game_record.log
- working_game_screeshot.png

## Comments:

The **Tui_Engine** class has some performance overhead. With some terminal emulators this can cause flickering.
A GPU accalerated terminal such as Kitty or Alacritty should be preferred. 

## played game record

As requested we made a record of a played game. This was achieved with *tee* and is under ./doc/played_game_record.log 
