#!/usr/bin/python3
from tkinter import *  # noqa: F403
from tkinter import ttk

root = Tk()  # noqa: F405
root.title("Hello World")
root.config(bg="#ccc")


def click():
    print("Hello World")


btn = ttk.Button(root, text="Hello World", command=click)
btn.pack()

e = ttk.Entry(root, width=20)
e.pack()

root.mainloop()
