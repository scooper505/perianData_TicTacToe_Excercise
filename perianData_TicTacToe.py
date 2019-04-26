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
from random import randint


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


# Function to randomly select a player to go first
def player_start():
    return randint(1,2)

# Function to check open space on board
def open_spot(board, position):
    return board[position] != "X" and board[position] != "O"



# Function to place player marker on board
def place_marker(board, marker):
    position = int(input("place a marker on the board "))
    
    while position not in range(1,10) or not open_spot(board, position):
        if position not in range(1,10):
            print("Invalid Entry --- Select Again")
            position = int(input("place a marker on the board "))
        else:
            print("Position not available, select another position")
            position = int(input("place a marker on the board "))
    
    board[position] = marker
    return board


# Function to check if there is a winner after marker is placed
def winner_check(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or\
    (board[1] == board[2] == board[3] == marker) or\
    (board[4] == board[5] == board[6] == marker) or\
    (board[7] == board[8] == board[9] == marker) or\
    (board[1] == board[4] == board[7] == marker) or\
    (board[2] == board[5] == board[8] == marker) or\
    (board[3] == board[6] == board[9] == marker) or\
    (board[1] == board[5] == board[9] == marker) or\
    (board[3] == board[5] == board[7] == marker))



# Function to check if board is full
def full_board(board):
    total = 0
    for i in range(1,10):
       if not open_spot(board, i):
        total += 1
    return total == 9
        

# Function to replay game
def replay():
    return input("Do you want to play again (Yes/No)? ").upper()


# Function to play tic tac toe game
def play_TicTacToe():
    print("Welcome to Tic Tac Toe")
    
    
    while True:
        game_on = False
        while game_on == False:
            game_on = input("Are you ready to play?(Y/N) ").upper() == "Y"
# Provide Start Board
        GameBoard = ["#","1","2","3","4","5","6","7","8","9"]
# Have player select marker
        Player1_marker, Player2_marker = select_marker()
    
# Select a player to go first
        if player_start() == 1:
            print("El Jugador uno empezara! Vamos!")
            turn = "player1"
        else:
            print("El Jugador dos empezara! Vamos!")
            turn = "player2"

 

    #   Game play    
        while game_on == True:


            if turn == "player1":
                display_board(GameBoard)
                print("\n"+"Player 1 turn")
                place_marker(GameBoard, Player1_marker)
                if winner_check(GameBoard, Player1_marker):
                    print("Player uno wins!")
                    game_on = False
                else: 
                    if full_board(GameBoard):
                        print("It is a tie")
                        break
                    else:
                        turn = "player2"

            if turn == "player2":
                display_board(GameBoard)
                print("\n"+"Player 2 turn")
                place_marker(GameBoard, Player2_marker)
                if winner_check(GameBoard, Player2_marker):
                    print("Player dos wins!")
                    game_on = False
                else:
                    if full_board(GameBoard):
                        print("It is a tie")
                        break
                    else:
                        turn = "player1"
                    
            
        if replay() == "N":
            break


play_TicTacToe()
# print("Hello World")