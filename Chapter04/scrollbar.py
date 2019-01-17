try:
    from tkinter import *   # Python 3
except ImportError:
    from Tkinter import *   # Python 2

root = Tk()
root.option_readfile('optionDB')
root.title('Scrollbar')
list = Listbox(root, height=6, width=15)
scroll = Scrollbar(root, command=list.yview)
list.configure(yscrollcommand=scroll.set)
list.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
for item in range(30):
    list.insert(END, item)
root.mainloop()

