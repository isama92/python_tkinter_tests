# Pack

from tkinter import Tk, Frame, Label, Button, LEFT, BOTTOM


def test1():
    root = Tk()
    root.title('Test 1 - Pack')

    bottomFrame = Frame(root)
    topFrame = Frame(root)

    label1 = Label(topFrame, text='I\'m the title label')
    label2 = Label(bottomFrame, text='I\'m the bottom label')
    button1 = Button(topFrame, text='Button 1', fg='red')
    button2 = Button(topFrame, text='Button 2', fg='blue')
    button3 = Button(topFrame, text='Button 3', fg='green')
    button4 = Button(bottomFrame, text='Button 4', fg='purple')

    bottomFrame.pack(side=BOTTOM)
    topFrame.pack()

    label1.pack()
    label2.pack(side=LEFT)
    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack(side=LEFT)
    button4.pack()

    root.mainloop()
