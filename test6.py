# Toolbar

from tkinter import Tk, Menu, Frame, Button, LEFT, TOP, X


def do_something():
    print('do something')


def test6():
    root = Tk()
    root.title('Test 6 - Toolbar')

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

    root.mainloop()
