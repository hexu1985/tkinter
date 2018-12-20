try:
    from tkinter import Label, mainloop   # Python 3
except ImportError:
    from Tkinter import Label, mainloop   # Python 2

aWidget = Label(None, text='How little code dose it need?')
aWidget.pack()
aWidget.mainloop()
