import tkinter


def tkinterSetup():
    root = tkinter.Tk()
    return root


def createLabel(root, text):
    my_label = tkinter.Label(
        master=root,
        text=text
    )
    return my_label


def main():

    running_status = {
        'frame': True
    }

    # FRAME
    if running_status['frame']:
        root = tkinterSetup()
        text_label = createLabel(root, 'Hello World!')
        text_label.pack()
        root.mainloop()


if __name__ == "__main__":
    main()
