# Tic Tac Toe with Numpy

Here is a Python-based version of that game you probably loved for at least 20 minutes when you were 6 years old: Tic Tac Toe.  I created this game for an assignment in my Python class.  I hadn't used Numpy much before this, so it was a good introduction to the library.  The three requirements were as follows:
* Track the state of the game
* Allow players to choose the position they want to place their X or O symbol
* Check for victory and end the game when either a win or a tie occurs

Tic tac toe is turn-based and essentially the same loop over and over again, so I needed to write a script for a recurring action, which was a first for me.  I have generally only needed to write code for data exploration or something else that only needs to run one time.  The game uses four functions to initialize the game, start each turn, check for victory after each turn, and invite the player to begin another game after the previous game ends.  This was also my first attempt at writing doc strings, so feel free to take a look and see if they make sense to you! :)

The script uses Numpy arrays to store and display the game board.  There was not a requirement to make the board pretty, so I just made it functional and displayed the game board array instead of drawing up a grid.  The script also uses Numpy to store the game score.  Because there are only two players, I decided the easiest way to track points would be to make each X equal to 1 and each O equal to -1.  That way, if any row, column, or diagonal summed to 3 or -3, the script could easily determine victory without having to store a separate score for each player. #KeepItSimple
