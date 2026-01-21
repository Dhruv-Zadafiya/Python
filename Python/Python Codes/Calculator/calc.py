import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

win = tk.Tk()
win.title('Calculator')

frame = tk.Frame(win, bg="skyblue", padx=10)
frame.pack()

entry = tk.Entry(frame, relief=SUNKEN, borderwidth=3, width=30, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, ipady=5, pady=5)

def click(num):
    entry.insert(tk.END, num)

def equal():
    try:
        res = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, res)
    except:
        tk.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('//', 5, 2), ('**', 5, 3),
]



for txt, r, c in buttons:
    tk.Button(frame, text=txt, padx=15, pady=10, width=5, font=("Arial", 12),
              command=lambda t=txt: click(t)).grid(row=r, column=c, pady=2)

tk.Button(frame, text="Clear", padx=15, pady=10, width=11, font=("Arial", 12), command=clear).grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(frame, text="=", padx=15, pady=10, width=11, font=("Arial", 12), command=equal).grid(row=6, column=2, columnspan=2, pady=5)

win.mainloop()
