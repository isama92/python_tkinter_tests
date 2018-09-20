# Grid

from tkinter import Tk, Label, Button, E, W


def test2():
    root = Tk()
    root.title('Test 2 - Grid')

    label1 = Label(root, text='I\'m the title label')
    label2 = Label(root, text='I\'m the bottom label')
    button1 = Button(root, text='Button 1', fg='red')
    button2 = Button(root, text='Button 2', fg='blue')
    button3 = Button(root, text='Button 3', fg='green')
    button4 = Button(root, text='Button 4', fg='purple')

    label1.grid(row=0, column=0)
    label2.grid(row=0, column=2)
    button1.grid(row=0, column=1)
    button2.grid(row=1, column=2, sticky=W)
    button3.grid(row=1, column=0, sticky=E)
    button4.grid(row=1, column=1)

    root.mainloop()
