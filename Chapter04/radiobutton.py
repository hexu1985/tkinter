try:
    from tkinter import *   # Python 3
except ImportError:
    from Tkinter import *   # Python 2

root = Tk()
root.option_readfile('optionDB')
root.title('Radiobutton')

fruit=[('Passion fruit', 1), ('Loganberries', 2), ('Mangoes in syrup', 3),
       ('Oranges', 4), ('Apples', 5), ('Grapefruit', 6)]
var = IntVar()
for text, value in fruit:
    Radiobutton(root, text=text, value=value, variable=var).pack(anchor=W)
var.set(3)
root.mainloop()

