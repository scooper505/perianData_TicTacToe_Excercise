# Perian Data Tic Tac Toe Excercise
# Complete a tic tac toe game


# To-Do:
# Create board
# function to place a marker on the board
# function to set marker for each user
# function to select who goes first
# function to check if board is full
# function to check if there is a winner


# Import Dependencies
import random


# Function to Display board


def display_board(board):
    
    print("\n")
    print(" "+board[1]+" | "+ board[2]+" | "+board[3]+" ")
    print("---|---|---")
    print(" "+board[4]+" | "+ board[5]+" | "+board[6]+" ")
    print("---|---|---")
    print(" "+board[7]+" | "+ board[8]+" | "+board[9]+" ")
    print("\n")


# Fucntion to prompt and assign user a board marker
def select_marker():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player 1, select a marker (X/O)? ").upper()
    if marker == "X":
        player1_marker = "X"
        player2_marker = "O"
    else:
        player1_marker = "O"
        player2_marker = "X"
    
    print("Player 1 will be "+player1_marker)
    print("Player 2 will be "+player2_marker)
    return player1_marker, player2_marker

# test_board = ["#","X","O","X","O","X","O","X","O","&"]
test_board = [" "]*10

display_board(test_board)

player1_marker, player2_marker = select_marker()
print(player1_marker)
