import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.mode = None
        self.scores = {"X": 0, "O": 0}
        self.create_mode_selection()

    def create_mode_selection(self):
        self.clear_window()
        tk.Label(self.root, text="Select Game Mode", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Player vs Player", command=self.start_pvp, font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Player vs Computer", command=self.start_pvc, font=("Arial", 12)).grid(row=1, column=1, padx=5, pady=5)

    def start_pvp(self):
        self.mode = "pvp"
        self.start_game()

    def start_pvc(self):
        self.mode = "pvc"
        self.start_game()

    def start_game(self):
        self.clear_window()
        self.board = [""] * 9
        self.current_player = "X"
        
        # Score display
        self.score_label = tk.Label(self.root, text=f"X: {self.scores['X']}  O: {self.scores['O']}", font=("Arial", 12))
        self.score_label.grid(row=0, column=0, columnspan=3)

        # Game board
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2,
                               command=lambda x=i*3+j: self.button_click(x))
                btn.grid(row=i+1, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

        # Control buttons
        tk.Button(self.root, text="Restart", command=self.restart, font=("Arial", 12)).grid(row=4, column=0, pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 12)).grid(row=4, column=2, pady=10)

    def button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index//3][index%3].config(text=self.current_player)
            
            if self.check_winner():
                self.scores[self.current_player] += 1
                self.score_label.config(text=f"X: {self.scores['X']}  O: {self.scores['O']}")
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.create_mode_selection()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.create_mode_selection()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.mode == "pvc" and self.current_player == "O":
                    self.computer_move()

    def computer_move(self):
        available = [i for i, spot in enumerate(self.board) if spot == ""]
        if available:
            move = random.choice(available)
            self.button_click(move)

    def check_winner(self):
        # Check rows, columns, diagonals
        for i in range(3):
            if self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] != "":
                return True
            if self.board[i] == self.board[i+3] == self.board[i+6] != "":
                return True
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        return False

    def restart(self):
        self.create_mode_selection()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()