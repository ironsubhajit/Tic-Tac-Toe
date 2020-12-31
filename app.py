import tkinter as tk
from tkinter import ttk, messagebox


root = tk.Tk()
root.geometry("530x400")
btn1 = ttk.Button(root, text='', command=lambda : button_pressed(1))
btn2 = ttk.Button(root, text='', command=lambda : button_pressed(2))
btn3 = ttk.Button(root, text='', command=lambda : button_pressed(3))
btn4 = ttk.Button(root, text='', command=lambda : button_pressed(4))
btn5 = ttk.Button(root, text='', command=lambda : button_pressed(5))
btn6 = ttk.Button(root, text='', command=lambda : button_pressed(6))
btn7 = ttk.Button(root, text='', command=lambda : button_pressed(7))
btn8 = ttk.Button(root, text='', command=lambda : button_pressed(8))
btn9 = ttk.Button(root, text='', command=lambda : button_pressed(9))

btn1.grid(row=0, column=0, ipadx=50, ipady=50)
btn2.grid(row=0, column=1, ipadx=50, ipady=50)
btn3.grid(row=0, column=2, ipadx=50, ipady=50)
btn4.grid(row=1, column=0, ipadx=50, ipady=50)
btn5.grid(row=1, column=1, ipadx=50, ipady=50)
btn6.grid(row=1, column=2, ipadx=50, ipady=50)
btn7.grid(row=2, column=0, ipadx=50, ipady=50)
btn8.grid(row=2, column=1, ipadx=50, ipady=50)
btn9.grid(row=2, column=2, ipadx=50, ipady=50)

player = 1


def check_winner():
    if (
            btn1['text'] == 'o' and btn2['text'] == 'o' and btn3['text'] == 'o' or
            btn4['text'] == 'o' and btn5['text'] == 'o' and btn6['text'] == 'o' or
            btn7['text'] == 'o' and btn8['text'] == 'o' and btn9['text'] == 'o' or
            btn1['text'] == 'o' and btn5['text'] == 'o' and btn9['text'] == 'o' or
            btn7['text'] == 'o' and btn5['text'] == 'o' and btn3['text'] == 'o' or
            btn1['text'] == 'o' and btn4['text'] == 'o' and btn7['text'] == 'o' or
            btn2['text'] == 'o' and btn5['text'] == 'o' and btn8['text'] == 'o' or
            btn3['text'] == 'o' and btn6['text'] == 'o' and btn9['text'] == 'o'
    ):
        messagebox._show("Winner of The Game", "Player \'o\' is the winner")
    elif (
            btn1['text'] == 'x' and btn2['text'] == 'x' and btn3['text'] == 'x' or
            btn4['text'] == 'x' and btn5['text'] == 'x' and btn6['text'] == 'x' or
            btn7['text'] == 'x' and btn8['text'] == 'x' and btn9['text'] == 'x' or
            btn1['text'] == 'x' and btn5['text'] == 'x' and btn9['text'] == 'x' or
            btn7['text'] == 'x' and btn5['text'] == 'x' and btn3['text'] == 'x' or
            btn1['text'] == 'x' and btn4['text'] == 'x' and btn7['text'] == 'x' or
            btn2['text'] == 'x' and btn5['text'] == 'x' and btn8['text'] == 'x' or
            btn3['text'] == 'x' and btn6['text'] == 'x' and btn9['text'] == 'x'
    ):
        messagebox._show("Winner of The Game", "Player \'x\' is the winner")


def button_pressed(button_number):
    global player
    if player == 1:
        if button_number == 1:
            btn1.config(text='x')
            player = 2
        elif button_number == 2:
            btn2.config(text='x')
            player = 2
        elif button_number == 3:
            btn3.config(text='x')
            player = 2
        elif button_number == 4:
            btn4.config(text='x')
            player = 2
        elif button_number == 5:
            btn5.config(text='x')
            player = 2
        elif button_number == 6:
            btn6.config(text='x')
            player = 2
        elif button_number == 7:
            btn7.config(text='x')
            player = 2
        elif button_number == 8:
            btn8.config(text='x')
            player = 2
        elif button_number == 9:
            btn9.config(text='x')
            player = 2
    elif player == 2:
        if button_number == 1:
            btn1.config(text='o')
            player = 1
        elif button_number == 2:
            btn2.config(text='o')
            player = 1
        elif button_number == 3:
            btn3.config(text='o')
            player = 1
        elif button_number == 4:
            btn4.config(text='o')
            player = 1
        elif button_number == 5:
            btn5.config(text='o')
            player = 1
        elif button_number == 6:
            btn6.config(text='o')
            player = 1
        elif button_number == 7:
            btn7.config(text='o')
            player = 1
        elif button_number == 8:
            btn8.config(text='o')
            player = 1
        elif button_number == 9:
            btn9.config(text='o')
            player = 1
    check_winner()


root.mainloop()
