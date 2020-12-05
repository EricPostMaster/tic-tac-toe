import numpy as np
import time
import sys

def initialize():
    """
    This function creates all of the basic objects needed for Tic Tac Toe.
    spaces is the 3x3 array that becomes the game board
    score is the 3x3 array that is the numeric equivalent of the game board
    rc_scores holds the sums of each row and column for checking for wins
    available is the list of remaining available spaces
    turn_counter increments by 1 with each turn

    Returns
    -------
    None.

    """
    
    global spaces
    global score
    global available
    global turn_counter
    global rc_scores
    
    # This is the Tic Tac Toe board
    spaces = np.array([["A1","B1","C1"],["A2","B2","C2"],["A3","B3","C3"]])
    
    # This is a numeric version of the board used for keeping score
    score = np.array([[0,0,0],[0,0,0],[0,0,0]])
    
    # This list is used for tracking the row and column total scores
    rc_scores = [0,0,0,0,0,0]

    # List of spaces available in current game
    available = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]

    # Counts what turn the game is on to determine if it is X or O's turn
    turn_counter = 1

def check_win():
    """
    This function converts the players' inputs into numbers for the score object
    It also updates the rc_scores and checks to see if there are any rows,
        columns, or diagonals that add up to 3 (for X's) or -3 (for O's) to
        determine victory or a tie.

    Returns
    -------
    None.

    """
    
    global spaces
    global score
    global available
    global turn_counter
    global position
    global rc_scores

    # Convert position selection into numeric row and column coordinate
    # Note, they both subtract 1 because the index starts at 0
    score_row = int(position[1])-1
    score_col = ord(position.lower()[0])-96-1  # This is converting the letter to a number

    # If turn_counter is odd, then a 1 is placed on the score board for X
    # If turn_counter is even, then a -1 is placed on the score board for O
    if turn_counter % 2 != 0:
        score[int(score_row)][int(score_col)] = 1
    elif turn_counter % 2 == 0:
        score[int(score_row)][int(score_col)] = -1

    # Sum the values in each row and column
    row_scores = score.sum(axis=0)
    col_scores = score.sum(axis=1)

    # Concatenate rows and columns into a single array
    rc_scores = np.concatenate((row_scores, col_scores), axis=0)

    # Loop checks for rows and columns that add to either 3 (X victory) or -3 (O victory)
    for rc in rc_scores:
        if rc >= 3:
            print("X wins!")
            play_again()
        elif rc <= -3:
                print("O wins!")
                play_again()
        else: continue

    # This loop checks diagonals for victory
    if score[0][0] + score[1][1] + score[2][2] == 3 or score[2][0] + score[1][1] + score[0][2] == 3:
        print("X wins!")
        play_again()
    elif score[0][0] + score[1][1] + score[2][2] == -3 or score[2][0] + score[1][1] + score[0][2] == -3:
        print("O wins!")
        play_again()  
    
def turn():
    """
    This function is the workhorse. It prompts the player for input, validates
        that input as available, updates the spaces object (the game board), 
        and calls the check_win() and play_again() functions as needed.

    Returns
    -------
    None.

    """
    
    global spaces
    global score
    global available
    global turn_counter
    global position
    global rc_scores
    
    # Ends the game if there is a tie
    if turn_counter == 10:
        print("\nGame Over! Tie game.")
        play_again()
    
    # Starts the game by displaying the game board and telling X to go first
    if turn_counter == 1:
        print("Let's play Tic Tac Toe!\n\nX makes the first move.\n\nPlease select from the following:\n", spaces)
    
    # Player input to select board position
    position = input( "\nChoose a position: " )

    # Player position converted to upper case to match spaces array
    coordinate = str(position.upper())

    # This is where most of the action happens
    if position.upper() in spaces:     # Check to see if the space exists at all
        available.remove(position.upper()) # Remove the space from the available list

        # If odd, add an X to the board.  If even, add an O.
        if turn_counter % 2 != 0:
            spaces = np.where(spaces==coordinate,"X",spaces)
        elif turn_counter % 2 == 0:
            spaces = np.where(spaces==coordinate,"O",spaces)

        # Print the new board
        print("\n", spaces,"\n")

        # Check for victory
        check_win()

        # Increment the turn counter to switch to the other player
        turn_counter = turn_counter +1

        # Delay becuase I feel like it makes the game easier to follow
        time.sleep(.5)

        # Tell players whose turn it is
        if turn_counter % 2 != 0: # turn_counter was incremented before this, so it should never be 1 here
            print("It's X's turn")
        elif turn_counter % 2 == 0 and turn_counter < 10: print("It's O's turn")

    # If the player's entry is not an available space, show the available list
    else: print("\nOops, that is not a valid selection.\n\nPlease choose from the following:\n", available,"\n", end='\r')
    
    # Next player's turn
    turn()
    
def play_again():
    """
    This function prompts the user to play again or quit.  Nothing too crazy!

    Returns
    -------
    None.

    """
# Ends the game without asking if you want to play again    
    time.sleep(1.5)
    sys.exit("\nThanks for playing!")
    
# Uncomment these things if you would like to prompt to play again
    # global turn_counter

    # # Ask if the players would like to play again
    # play = input("\nWould you like to play again? Y/N  ")

    # # If anything other than the letter 'n' (in any case) is entered,
    # # a new game will start.  Otherwise, the game ends.
    # if play.upper() != "N":
    #     initialize()
    #     turn()
    # else: sys.exit("\nFine. I didn't want to play again either.")

# These start the game
initialize()  
turn()