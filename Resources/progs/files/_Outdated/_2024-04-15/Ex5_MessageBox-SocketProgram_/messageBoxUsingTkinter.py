from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")


def msg():
    messagebox.showwarning("Alert Box", "Stop Virus found")


butn = Button(root, text="ok", command=msg)
butn.place(x=100, y=100)
root.mainloop()
