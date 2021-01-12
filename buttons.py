import tkinter


def tkinterSetup():
    root = tkinter.Tk()
    return root


def createButton(root, text):
    my_button = tkinter.Button(
        master=root,
        text=text
    )
    return my_button


def createDiabledButton(root, text):
    my_button = tkinter.Button(
        master=root,
        text=text,
        state=tkinter.DISABLED
    )
    return my_button


def main():

    running_status = {
        'button': True,
    }

    # BUTTON
    if running_status['button']:
        root_button = tkinterSetup()
        button = createButton(root_button, 'Click me')
        disabled_button = createDiabledButton(
            root_button,
            'Click me if you can'
        )
        button.pack()
        disabled_button.pack()
        root_button.mainloop()


if __name__ == "__main__":
    main()
