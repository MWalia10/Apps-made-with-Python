from tkinter import *

window = Tk()

def kg_convert():
    kg = float(e1_value.get())
    gram = round(kg*1000, 2)
    pound = round(kg*2.20462, 2)
    ounce = round(kg*35.274, 2)
    t1.delete("1.0", END)
    t2.delete("1.0", END)
    t3.delete("1.0", END)
    t1.insert(END, f"{gram} grams")
    t2.insert(END, f"{pound} pounds")
    t3.insert(END, f"{ounce} ounces")
l1=Label(window,text="Kg")
l1.grid(row=0,column=0)
b1 = Button(window, text = "Convert", command = kg_convert)
b1.grid(row = 0, column = 2)
e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)
t1 = Text(window, height = 1, width = 15)
t1.grid(row = 1, column = 0)
t2 = Text(window, height = 1, width = 15)
t2.grid(row = 1, column = 1)
t3 = Text(window, height = 1, width = 15)
t3.grid(row = 1, column = 2)


window.mainloop()