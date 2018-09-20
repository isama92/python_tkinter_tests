# Shapes and Graphics

from tkinter import Tk, Canvas, ALL


def test9():
    root = Tk()
    root.title('Test 9 - Shapes and Graphics')

    width = 800
    height = 600
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()

    blackline = canvas.create_line(0, 0, width, height)
    redline = canvas.create_line(0, height, width, 0, fill='red')
    greenbox = canvas.create_rectangle(width/4, height/4, (width/2 + width/4), (height/2 + height/4), fill='green')

    canvas.delete(redline)
    # canvas.delete(ALL)

    blackline2 = canvas.create_line(0, height, width, 0)

    root.mainloop()
