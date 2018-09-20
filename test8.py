# MessageBox

from tkinter import Tk, Button, messagebox


def show_msg():
    # messagebox.showinfo('Do something', 'Hello, I am doing something!')
    if messagebox.askquestion('Do something', 'Hello, am I doing something?') == 'yes':
        print('I am doing something')
    else:
        print('I am not doing something')


def test8():
    root = Tk()
    root.title('Test 8 - MessageBox')

    button = Button(root, text='Button', command=show_msg)
    button.pack()

    root.mainloop()
