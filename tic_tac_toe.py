# import tkinter as tk
# from tkinter import messagebox
# import random

# root = tk.Tk()
# root.title("Tic Tac Toe")

# player = "X"
# board = ["", "", "", "", "", "", "", "", ""]
# score_x = 0
# score_o = 0

# def button_click(index):
#     global player
#     if board[index] == "":
#         board[index] = "X"
#         buttons[index].config(text="X")
        
#         if check_win():
#             global score_x
#             score_x += 1
#             score_label.config(text=f"Player: {score_x}  Computer: {score_o}")
#             messagebox.showinfo("Game Over", "You win!")
#             reset_board()
#         elif "" not in board:
#             messagebox.showinfo("Game Over", "Tie!")
#             reset_board()
#         else:
#             computer_move()

# def computer_move():
#     available = [i for i in range(9) if board[i] == ""]
#     if available:
#         move = random.choice(available)
#         board[move] = "O"
#         buttons[move].config(text="O")
        
#         if check_win():
#             global score_o
#             score_o += 1
#             score_label.config(text=f"Player: {score_x}  Computer: {score_o}")
#             messagebox.showinfo("Game Over", "Computer wins!")
#             reset_board()
#         elif "" not in board:
#             messagebox.showinfo("Game Over", "Tie!")
#             reset_board()

# def check_win():
#     if board[0] == board[1] == board[2] != "":
#         return True
#     if board[3] == board[4] == board[5] != "":
#         return True
#     if board[6] == board[7] == board[8] != "":
#         return True
#     if board[0] == board[3] == board[6] != "":
#         return True
#     if board[1] == board[4] == board[7] != "":
#         return True
#     if board[2] == board[5] == board[8] != "":
#         return True
#     if board[0] == board[4] == board[8] != "":
#         return True
#     if board[2] == board[4] == board[6] != "":
#         return True
#     return False

# def reset_board():
#     global board, player
#     board = ["", "", "", "", "", "", "", "", ""]
#     player = "X"
#     for btn in buttons:
#         btn.config(text="")

# def exit_game():
#     root.quit()

# score_label = tk.Label(root, text=f"Player: {score_x}  Computer: {score_o}", font=("Arial", 12))
# score_label.grid(row=0, column=0, columnspan=3)

# buttons = []
# for i in range(9):
#     btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda x=i: button_click(x))
#     btn.grid(row=(i//3)+1, column=i%3)
#     buttons.append(btn)

# restart_btn = tk.Button(root, text="Restart", font=("Arial", 12), command=reset_board)
# restart_btn.grid(row=4, column=0)

# exit_btn = tk.Button(root, text="Exit", font=("Arial", 12), command=exit_game)
# exit_btn.grid(row=4, column=2)

# root.mainloop()

#################################################################################################
import random

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_move():
    move = input("اختر رقم من 1 لـ 9: ")
    if move in board:
        index = board.index(move)
        board[index] = "X"
    else:
        print("المكان مش فاضي أو الرقم غلط، جرّب تاني.")
        player_move()

def computer_move():
    available = [cell for cell in board if cell not in ["X", "O"]]
    if available:
        move = random.choice(available)
        index = board.index(move)
        board[index] = "O"

def check_win(player):
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

print("Welcome to Tic Tac Toe!")

while True:
    print_board()
    player_move()
    if check_win("X"):
        print_board()
        print("ألف مبروك! أنت كسبت.")
        break
    if all(cell in ["X", "O"] for cell in board):
        print_board()
        print("تعادل.")
        break

    computer_move()
    if check_win("O"):
        print_board()
        print("الكمبيوتر كسب.")
        break
    if all(cell in ["X", "O"] for cell in board):
        print_board()
        print("تعادل.")
        break
