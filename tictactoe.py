import random
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
current_player = 'X'

def display_board():
    print("Tic Tac Toe - Single Player")
    print("Instructions:")
    print("Enter a number between 1 and 9 to make your move.")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print()
    print ("Current Board:")
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner():
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False

def is_board_full():
    for row in board:
        if ' ' in row:
            return False
    return True

def player_move():
    global current_player
    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): "))
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3

                if board[row][col] == ' ':
                    board[row][col] = current_player
                    break
                else:
                    print("Cell already occupied. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ai_move():
    global current_player

    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = current_player

while True:
    display_board()
    if current_player == 'X':
        player_move()
    else:
        ai_move()
    if check_winner():
        display_board()
        print(f"Player {current_player} wins!")
        break
    elif is_board_full():
        display_board()
        print("It's a tie!")
        break
    current_player = 'O' if current_player == 'X' else 'X'
