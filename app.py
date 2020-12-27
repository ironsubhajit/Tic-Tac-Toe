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


def button_pressed(button_number):
    global player
    if player == 1:
        if buttonNumber == 1:
            btn1.config(text='x')
            player = 2
        elif buttonNumber == 2:
            btn2.config(text='x')
            player = 2
        elif buttonNumber == 3:
            btn3.config(text='x')
            player = 2
        elif buttonNumber == 4:
            btn4.config(text='x')
            player = 2
        elif buttonNumber == 5:
            btn5.config(text='x')
            player = 2
        elif buttonNumber == 6:
            btn6.config(text='x')
            player = 2
        elif buttonNumber == 7:
            btn7.config(text='x')
            player = 2
        elif buttonNumber == 8:
            btn8.config(text='x')
            player = 2
        elif buttonNumber == 9:
            btn9.config(text='x')
            player = 2
    elif player == 2:
        if buttonNumber == 1:
            btn1.config(text='o')
            player = 1
        elif buttonNumber == 2:
            btn2.config(text='o')
            player = 1
        elif buttonNumber == 3:
            btn3.config(text='o')
            player = 1
        elif buttonNumber == 4:
            btn4.config(text='o')
            player = 1
        elif buttonNumber == 5:
            btn5.config(text='o')
            player = 1
        elif buttonNumber == 6:
            btn6.config(text='o')
            player = 1
        elif buttonNumber == 7:
            btn7.config(text='o')
            player = 1
        elif buttonNumber == 8:
            btn8.config(text='o')
            player = 1
        elif buttonNumber == 9:
            btn9.config(text='o')
            player = 1


root.mainloop()
