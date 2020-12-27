import tkinter as tk
from tkinter import ttk, messagebox


def buttonPressed(buttonNumber):
    pass

root = tk.Tk()
root.geometry("500x300")
btn1 = ttk.Button(root, text='', command=lambda : buttonPressed(1))
btn2 = ttk.Button(root, text='', command=lambda : buttonPressed(2))
btn3 = ttk.Button(root, text='', command=lambda : buttonPressed(3))
btn4 = ttk.Button(root, text='', command=lambda : buttonPressed(4))
btn5 = ttk.Button(root, text='', command=lambda : buttonPressed(5))
btn6 = ttk.Button(root, text='', command=lambda : buttonPressed(6))
btn7 = ttk.Button(root, text='', command=lambda : buttonPressed(7))
btn8 = ttk.Button(root, text='', command=lambda : buttonPressed(8))
btn9 = ttk.Button(root, text='', command=lambda : buttonPressed(9))


root.mainloop()
