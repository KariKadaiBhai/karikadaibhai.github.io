from tkinter import *
from datetime import date


def calculator():
    global result
    result = str(entry.get())
    today = date.today()
    dob_data = result.split("/")
    day = int(dob_data[0])
    month = int(dob_data[1])
    year = int(dob_data[2])
    dob = date(year, month, day)
    numberOfDays = (today - dob).days
    age = numberOfDays // 365
    label = Label(root, text="Your age is " + str(age))
    label.pack()


root = Tk()
root.geometry("300x300")
infoLabel = Label(root, text="Enter your date of birth [DD/MM/YYYY]:")
infoLabel.pack()
entry = Entry(root)
entry.pack()
button = Button(root, text="Age", command=calculator)
button.pack()
root.mainloop()
