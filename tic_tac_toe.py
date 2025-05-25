from tkinter import *

# Check for a win
def checkwinner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if board is full
def is_boardfull(board):
    return all(all(cell != ' ' for cell in row) for row in board)

# Minimax algorithm
def min_max(board, depth, is_maximize):
    if checkwinner(board, 'X'):
        return -1
    if checkwinner(board, 'O'):
        return 1
    if is_boardfull(board):
        return 0

    if is_maximize:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = min_max(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = min_max(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# Find best move for AI
def best_move(board):
    best_val = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = min_max(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# Make player move
def make_move(row, col):
    if board[row][col] == ' ' and status_label['text'] == '':
        board[row][col] = 'X'
        buttons[row][col].config(text='X', fg='dark blue')
        if checkwinner(board, 'X'):
            status_label.config(text="You win!")
            disable_all_buttons()
        elif is_boardfull(board):
            status_label.config(text="It's a draw!")
            disable_all_buttons()
        else:
            ai_move()
    elif status_label['text'] == '':
        status_label.config(text="Invalid move!")

# Make AI move
def ai_move():
    move = best_move(board)
    if move:
        row, col = move
        board[row][col] = 'O'
        buttons[row][col].config(text='O', fg='dark blue')
        if checkwinner(board, 'O'):
            status_label.config(text="AI wins!")
            disable_all_buttons()
        elif is_boardfull(board):
            status_label.config(text="It's a draw!")
            disable_all_buttons()

# Disable all buttons after game ends
def disable_all_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=DISABLED)

# GUI Setup
root = Tk()
root.title("Tic Tac Toe")
root.configure(bg='beige')

board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = []

# Create game buttons
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = Button(root, text=' ', font=('Arial', 30), width=5, height=2,
                        command=lambda row=i, col=j: make_move(row, col),
                        bg='beige', fg='dark blue')
        button.grid(row=i, column=j, padx=5, pady=5)
        row_buttons.append(button)
    buttons.append(row_buttons)

# Status label for game messages
status_label = Label(root, text='', font=('Arial', 20, 'bold'), bg='beige', fg='dark blue')
status_label.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()




        
                







