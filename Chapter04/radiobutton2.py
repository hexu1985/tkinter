try:
    from tkinter import *   # Python 3
except ImportError:
    from Tkinter import *   # Python 2

root = Tk()
root.option_readfile('optionDB')
root.title('Radiobutton')

cheese=[('Red Leicester', 1), ('Tilsit', 2), ('Caerphilly', 3),
       ('Stilton', 4), ('Emental', 5), ('Roquefort', 6), ('Brie', 7)]
var = IntVar()
for text, value in cheese:
    Radiobutton(root, text=text, value=value, variable=var,
                indicatoron=0).pack(anchor=W, fill=X, ipadx=18)
var.set(3)
root.mainloop()

