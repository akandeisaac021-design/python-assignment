def create_board():
    board =[[ 0  for _ in range(3)] for _ in range(3)]
    return board

def fill_board_with_placeholders_from_1_to_9(board):
    slot = 1
    for column in range(3):
        for row in range(3):
            board[column][row] = slot
            slot += 1
    return board

def print_board(board):
    for column in range(3):
        print(' ')
        print(' ', end='')
        for row in range(3):
            print("||", board[column][row], end=' || ')


def get_player_input(player_input):
    player_input = int(input(f"Player {player}, enter a number between 1 and 9: "))
    return player_input

def validate_player_input(player_input):
    while True:
            player_input = int(input(f"Player {player}, enter a number between 1 and 9: "))
            if player_input < 1 or player_input > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
            else:
                return player_input
            
def update_board(board, player_input, player):
    for column in range(3):
        for row in range(3):
            if board[column][row] == player_input:
                if player == 1:
                    board[column][row] = 'X'  
                else:
                    board[column][row] = 'O'
                return board
            
def check_row_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    return False


# def check_column_win():
#     for row in range(3):
#         for column in range(3):
#             if player ==1:
#                 if all(board[column])
