# General Information

This dir contains the projects documentation.
All source-code goes into the source-directory **"/src"**.

## Requirements

For running the game, a minimal terminal size is requiered. Please maximize the terminal. 

### For Windows Users

The defautl windows terminal is quite bad at rendering. 
Some flickering must be excpected. We would recommend the use of a gpu accalerated Terminal such as Kitty or Alacritty, but if a Windows environment is preferred we would recommend the new win11 terminal or powershell. 

## Files:

- [rules.md](https://github.com/FelixSchladt/kniffel/blob/main/doc/rules.md)

## Pylint errors

Sometimes pylint is jsut mistaken or makes no sense in our eyes.
This is the reason why two pylint errors persist. 

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
This class is just a wrapper for constants and therfore does not have any functions related to it.
I personally believe this is the neatest way to bundle these constants and therfore ignored pylint's
requirement.


## Comments:

The **TUI_ENGINE** class has some performance overhead. With some terminal emulators this can cause flickering.
A GPU accalerated terminal such as Kitty or Alacritty should be preferred. 





