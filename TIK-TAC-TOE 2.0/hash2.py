import sys
from tkinter import messagebox
import tkinter as tk

symbol = 'X'
root = tk.Tk()
root.withdraw() 

def homeMenu():
    option = messagebox.askquestion('Welcome', 'Would you like to play tic-tac-toe?')
    if option == 'yes':
        displayboard()
    else:
        sys.exit()

def button_callback(i, j, board,display):
    global symbol

    if board[i][j]["text"] == "":
        board[i][j]["text"] = symbol
        if symbol == "X":
            symbol = "O"
        else:
            symbol = "X"
    if verificationWinner(board):
        messagebox.showinfo("Result", "You win!")
        display.destroy()
        question()
    verificationCases(board, display)

def verificationWinner(board):
    return lineCheck(board) or columnCheck(board) or diagonalCheck(board)

def lineCheck(board):
    for i in range(len(board)):
        if all(verification['text']  == 'X' for verification in board[i]):
            return True
        elif all(verification['text'] == 'O' for verification in board[i]):
            return True
    
def columnCheck(board):
    for i in range(len(board)):
        column = [line[i] for line in board]
        if all(verification['text'] == 'X' for verification in column):
            return True
        elif all(verification['text'] == 'O' for verification in column):
            return True

def diagonalCheck(board):
    diagonal = [board[i][i]["text"] for i in range(len(board))]
    diagonalInverted = [board[i][len(board)-i-1]["text"] for i in range(len(board))]
    if all(verification == 'X' for verification in diagonal):
        return True
    elif all(verification == 'O'  for verification in diagonal):
        return True
    elif all(verification == 'X' for verification in diagonalInverted):
        return True
    elif all(verification == 'O'  for verification in diagonalInverted):
        return True
    
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    pos_x = (screen_width - width) // 2
    pos_y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

def displayboard():
    global symbol

    display = tk.Toplevel(root)
    display.title('TIC-TAC-TOE')
    display.iconbitmap('image/icon_app.ico')

    width = 600
    height = 600

    center_window(display, width, height)

    display.columnconfigure(0, weight=1)
    display.columnconfigure(1, weight=1)
    display.columnconfigure(2, weight=1)
    display.rowconfigure(0, weight=1)
    display.rowconfigure(1, weight=1)
    display.rowconfigure(2, weight=1)

    board = []
    for i in range(3):
        linha = []
        for j in range(3):
            button = tk.Button(display, text="", relief=tk.RIDGE, command=lambda i=i, j=j: button_callback(i, j, board, display), width=10, height=5, font=('Arial', 20), bg='black', fg='white', bd=0.5)
            button.grid(row=i, column=j,sticky="nsew")
            linha.append(button)
        board.append(linha)
    symbol = 'X'
    display.mainloop()

def verificationCases(board, display):
    verification = []
    for line in board:
        if all(word['text'] == 'X' or word['text'] == 'O' for word in line):
            verification.append(True)
        else:
            verification.append(False)
            break
    if all(verification == True for verification in verification):
        messagebox.showinfo("Result", "Game Over")
        display.destroy()
        question()

def question():
  option = messagebox.askquestion("Confirmation", "Would you like to play again?")
  if option == "yes":
    displayboard()
  else:
    sys.exit()

def main():
    homeMenu()

main()