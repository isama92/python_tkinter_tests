# Login

from tkinter import Tk, Label, Button, Entry, Checkbutton, E

mode = 1

def login(event):
    print('logging in...')

def test3():
    root = Tk()
    root.title('Test 3 - Login')

    labelUsername = Label(root, text='Username:')
    labelPassword = Label(root, text='Password:')

    entryUsername = Entry(root)
    entryPassword = Entry(root)

    rememberCheck = Checkbutton(root, text='Remember me')

    if mode == 0:
        buttonLogin = Button(root, text='Login', fg='red', command=login)
    elif mode == 1:
        buttonLogin = Button(root, text='Login', fg='red')
        buttonLogin.bind('<Button-1>', login)  # <Button-1>: Left click

    labelUsername.grid(row=0, column=0, sticky=E)
    labelPassword.grid(row=1, column=0, sticky=E)
    entryUsername.grid(row=0, column=1)
    entryPassword.grid(row=1, column=1)
    rememberCheck.grid(row=2, column=0, columnspan=2)
    buttonLogin.grid(row=3, column=0, columnspan=2)

    root.mainloop()
