import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("200x250")
root.title("Крестики-нолики")

buttons = list()
flag = True
move = 0


# ----- Создание кнопок -----
def pl_ground():
    global root
    global buttons
    buttons = []
    for i in range(9):
        button = tk.Button(root, text=str(i), height=4, width=8, command=lambda b=i: players_moves(b))
        button.grid(pady=1, row=i // 3, column=i % 3)
        buttons.append(button)


# ----- Функция проверки победы -----
def win_combinations(playground):
    comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]]

    for c in comb:
        if playground[c[0]] == "X" and playground[c[1]] == "X" and playground[c[2]] == "X":
            return "X"
        elif playground[c[0]] == "O" and playground[c[1]] == "O" and playground[c[2]] == "O":
            return "O"


# ----- Функция обработки клика -----
def players_moves(index):
    global flag
    global move
    if flag:
        buttons[index].config(text="X", bg="green1", state=tk.DISABLED)
        buttons[index] = "X"
        flag = False
        move += 1
    else:
        buttons[index].config(text="O", bg="green3", state=tk.DISABLED)
        buttons[index] = "O"
        flag = True
        move += 1

    if win_combinations(buttons) == "O":
        messagebox.showinfo("Победа!", "Победил O!")
    elif win_combinations(buttons) == "X":
        messagebox.showinfo("Победа!", "Победил X!")
    elif move == 9:

        messagebox.showinfo("Ничья!", "Игра окончена. Ничья!")


# ----- Сброс игры -----
restart = tk.Button(root, text="Новая игра", command=pl_ground)
restart.grid(row=3, column=0, columnspan=3, sticky="we")

if __name__ == "__main__":
    tk.mainloop()
