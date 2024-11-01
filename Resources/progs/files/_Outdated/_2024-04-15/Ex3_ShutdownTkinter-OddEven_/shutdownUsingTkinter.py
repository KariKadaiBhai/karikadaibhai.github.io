from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.geometry("300x300")


def shut():
    os.system("shutdown /s /t 1")


ttk = Button(root, text="SHUT DOWN", command=shut).pack()
root.mainloop()
