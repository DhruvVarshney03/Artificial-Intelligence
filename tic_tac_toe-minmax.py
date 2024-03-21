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

def check_winner(board, player):
    for row in board:
        if row.count(row[0]) == 3 and row[0] == player:
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for row, col in available_moves(board):
            board[row][col] = 'O'
            eval = minimax(board, depth + 1, False)
            board[row][col] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row, col in available_moves(board):
            board[row][col] = 'X'
            eval = minimax(board, depth + 1, True)
            board[row][col] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def ai_move(board):
    best_eval = float('-inf')
    best_move = None
    for row, col in available_moves(board):
        board[row][col] = 'O'
        eval = minimax(board, 0, False)
        board[row][col] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = (row, col)
    return best_move

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

def play_game():
    global current_player
    display_board()
    while not check_winner(board, 'X') and not check_winner(board, 'O') and not is_board_full(board):
        if current_player == 'X':
            player_move()
            current_player = 'O'
        else:
            move = ai_move(board)
            board[move[0]][move[1]] = 'O'
            current_player = 'X'
        display_board()
    if check_winner(board, 'O'):
        print("AI wins!")
    elif check_winner(board, 'X'):
        print("Player wins!")
    else:
        print("It's a tie!")

print("Dhruv Varshney \nA2305221157")
# Start the game
play_game()
