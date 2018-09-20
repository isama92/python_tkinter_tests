# Toolbar

from tkinter import Tk, Menu, Frame, Button, Label, LEFT, TOP, BOTTOM, X, SUNKEN, W


def do_something():
    print('do something')


def test7():
    root = Tk()
    root.title('Test 7 - Toolbar')

    menu = Menu()
    root.option_add('*tearOff', False)

    # Menu
    file = Menu(menu)
    file.add_command(label='Quit', command=root.quit)
    menu.add_cascade(label='File', menu=file)
    root.config(menu=menu)

    # Toolbar
    toolbar = Frame(root, bg='blue')
    insertButton = Button(toolbar, text='Insert', command=do_something)
    insertButton.pack(side=LEFT, padx=2, pady=2)
    printButton = Button(toolbar, text='Print', command=do_something)
    printButton.pack(side=LEFT, padx=2, pady=2)
    toolbar.pack(side=TOP, fill=X)

    # Statusbar
    statusbar= Frame(root, bd=1, relief=SUNKEN)
    statusbar.pack(side=BOTTOM, fill=X)
    statusLabel = Label(statusbar, text='File has been saved succesfully', anchor=W)
    statusLabel.pack(side=LEFT, fill=X)

    root.mainloop()
