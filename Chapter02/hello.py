try:
    from tkinter import Label, mainloop   # Python 3
except ImportError:
    from Tkinter import Label, mainloop   # Python 2

Label(text='This has to be the\nsimplest bit of code').pack()
mainloop()


