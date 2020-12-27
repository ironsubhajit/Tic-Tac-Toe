import tkinter as tk
from tkinter import ttk, messagebox


def button_pressed(buttonNumber):
    pass


root = tk.Tk()
root.geometry("530x400")
btn1 = ttk.Button(root, text='', command=lambda : buttonPressed(1))
btn2 = ttk.Button(root, text='', command=lambda : buttonPressed(2))
btn3 = ttk.Button(root, text='', command=lambda : buttonPressed(3))
btn4 = ttk.Button(root, text='', command=lambda : buttonPressed(4))
btn5 = ttk.Button(root, text='', command=lambda : buttonPressed(5))
btn6 = ttk.Button(root, text='', command=lambda : buttonPressed(6))
btn7 = ttk.Button(root, text='', command=lambda : buttonPressed(7))
btn8 = ttk.Button(root, text='', command=lambda : buttonPressed(8))
btn9 = ttk.Button(root, text='', command=lambda : buttonPressed(9))

btn1.grid(row=0, column=0, ipadx=50, ipady=50)
btn2.grid(row=0, column=1, ipadx=50, ipady=50)
btn3.grid(row=0, column=2, ipadx=50, ipady=50)
btn4.grid(row=1, column=0, ipadx=50, ipady=50)
btn5.grid(row=1, column=1, ipadx=50, ipady=50)
btn6.grid(row=1, column=2, ipadx=50, ipady=50)
btn7.grid(row=2, column=0, ipadx=50, ipady=50)
btn8.grid(row=2, column=1, ipadx=50, ipady=50)
btn9.grid(row=2, column=2, ipadx=50, ipady=50)

root.mainloop()
