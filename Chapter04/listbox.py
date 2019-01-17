try:
    from tkinter import *   # Python 3
except ImportError:
    from Tkinter import *   # Python 2

root = Tk()
root.option_readfile('optionDB')
root.title('Listbox')
list = Listbox(root, width=15)
list.pack()
for item in range(10):
    list.insert(END, item)
root.mainloop()

