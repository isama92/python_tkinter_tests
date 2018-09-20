# Class

from tkinter import Tk, Frame, Button, LEFT


class Test:
    def __init__(self, root):
        root.title('Test 4 - Class')
        frame = Frame(root)
        self.printButton = Button(frame, text='Print message', command=self.printMessage)
        self.quitButton = Button(frame, text='Quit', command=frame.quit)

        frame.pack()
        self.printButton.pack(side=LEFT)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('print message')


def test4():
    root = Tk()
    Test(root)
    root.mainloop()
