# !/usr/bin/python3
from tkinter import *

tkit = Tk()

frame = Frame(tkit, width=50, height=10)
text = Text()
text.insert(INSERT, "First Name")
E1 = Entry(tkit, bd = 10)
frame.bind(text,E1)
frame.bind(E1)
frame.pack()

# Lb1.insert(2, "Last Name")
# Lb1.insert(3, "Age")
# Lb1.insert(4, "Gender")
# Lb1.insert(5, "Hobby")
# Lb1.pack(side = LEFT)
tkit.mainloop()