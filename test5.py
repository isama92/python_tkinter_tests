# Menu

from tkinter import Tk, Menu


def do_something():
    print('do something')


def test5():
    root = Tk()
    root.title('Test 5 - Menu')

    menu = Menu()
    root.option_add('*tearOff', False)
    file = Menu(menu)
    edit = Menu(menu)

    file.add_command(label='Do something 1', command=do_something)
    file.add_command(label='Do something 2', command=do_something)
    file.add_separator()
    file.add_command(label='Quit', command=root.quit)

    edit.add_command(label='Do something 3', command=do_something)
    edit.add_command(label='Do something 4', command=do_something)

    menu.add_cascade(label='File', menu=file)
    menu.add_cascade(label='Edit', menu=edit)

    root.config(menu=menu)

    root.mainloop()
