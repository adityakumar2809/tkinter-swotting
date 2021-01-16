import tkinter


def tkinterSetup():
    root = tkinter.Tk()
    return root


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
