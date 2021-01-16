import tkinter
from tkinter import messagebox


def tkinterSetup():
    root = tkinter.Tk()
    return root


def popup():
    messagebox.showinfo('My Pop-Up', 'Hello World')
    messagebox.showwarning('My Pop-Up', 'Hello World')
    messagebox.showerror('My Pop-Up', 'Hello World')
    messagebox.askquestion('My Pop-Up', 'Hello World')
    messagebox.askokcancel('My Pop-Up', 'Hello World')


def createButton(root, text):
    my_button = tkinter.Button(
        master=root,
        text=text,
        command=popup
    )
    return my_button


def main():

    running_status = {
        'msg': True
    }

    # MESSAGE BOX
    if running_status['msg']:
        root = tkinterSetup()
        button = createButton(root, 'Pop-up')
        button.pack()
        root.mainloop()


if __name__ == "__main__":
    main()
