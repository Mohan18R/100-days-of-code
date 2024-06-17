import random

def display_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def player_move(board, player):
    if player == 'X':  # Human player
        while True:
            try:
                move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
                if board[move] == ' ':
                    board[move] = player
                    break
                else:
                    print("This spot is already taken.")
            except (IndexError, ValueError):
                print("Invalid move. Please enter a number between 1 and 9.")
    elif player == 'O':  # Computer player
        move = computer_move(board)
        board[move] = player

def computer_move(board):
    # Generate random move
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            return move

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6] 
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    return ' ' not in board

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    
    display_board(board)
    
    while True:
        player_move(board, current_player)
        display_board(board)
        
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("The game is a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()
