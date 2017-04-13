# TowersOfHanoi
This is a simple text based representation of the classic puzzle game Towers of Hanoi.
The user inputs how many disks they would like to play with, and then proceeds to use buttons to move those disks
from peg to peg. All data from the game is represented in text. Graphic user interface created from Python's tkinter modules.

There is an additionaly class in the main TwrHanoi file that shows a "perfect" game, played by the computer. User can
input how many disks the computer should solved the puzzle for.

NOTES:
    Game is now functional, and will recognize when a user has won, giving them 
         to play a new game or end the current session. Both of these options implement correctly. 
    Program does not check for larger disks being placed on top of smaller disks (which is not allowed in game play). This
         feature should be added in order for users to not cheat the game.
