import tkinter


def tkinterSetup():
    root = tkinter.Tk()
    return root


def createLabel(root):
    my_label = tkinter.Label(
        master=root,
        text='Hello World!'
    )
    return my_label


def main():
    root_basic = tkinterSetup()
    text_label = createLabel(root_basic)
    text_label.pack()
    root_basic.mainloop()


if __name__ == "__main__":
    main()
