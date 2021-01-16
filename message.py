import tkinter
from tkinter import messagebox


def tkinterSetup():
    root = tkinter.Tk()
    return root


def popup(root):
    response = messagebox.showinfo('My Pop-Up', 'Hello World')
    label = createLabel(root, f'showinfo: { response }')
    label.pack()
    response = messagebox.showwarning('My Pop-Up', 'Hello World')
    label = createLabel(root, f'showwarning: { response }')
    label.pack()
    response = messagebox.showerror('My Pop-Up', 'Hello World')
    label = createLabel(root, f'showerror: { response }')
    label.pack()
    response = messagebox.askquestion('My Pop-Up', 'Hello World')
    label = createLabel(root, f'askquestion: { response }')
    label.pack()
    response = messagebox.askokcancel('My Pop-Up', 'Hello World')
    label = createLabel(root, f'askokcancel: { response }')
    label.pack()
    response = messagebox.askretrycancel('My Pop-Up', 'Hello World')
    label = createLabel(root, f'askretrycancel: { response }')
    label.pack()
    response = messagebox.askyesno('My Pop-Up', 'Hello World')
    label = createLabel(root, f'askyesno: { response }')
    label.pack()
    response = messagebox.askyesnocancel('My Pop-Up', 'Hello World')
    label = createLabel(root, f'askyesnocancel: { response }')
    label.pack()


def createButton(root, text):
    my_button = tkinter.Button(
        master=root,
        text=text,
        command=lambda: popup(root)
    )
    return my_button


def createLabel(root, text):
    my_label = tkinter.Label(
        master=root,
        text=text
    )
    return my_label


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
