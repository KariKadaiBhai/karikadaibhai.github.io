from tkinter import *

window = Tk()

label = Label(window, text="Mobile OS")
label.pack()

list = Listbox(window, bg="pink")
list.insert(1, "Android")
list.insert(2, "iOS")
list.insert(3, "Blackberry")
list.insert(4, "Symbian")
list.pack()

window.config(bg="White")
window.geometry("300x300")
window.title("LIST")

window.mainloop()
