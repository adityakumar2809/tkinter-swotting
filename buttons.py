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


def createPaddedButton(root, text):
    my_button = tkinter.Button(
        master=root,
        text=text,
        padx=20,
        pady=10
    )
    return my_button


def createCommandButton(root, text):
    my_button = tkinter.Button(
        master=root,
        text=text,
        command=lambda: showLabelOnClick(root)
    )
    return my_button


def showLabelOnClick(root):
    text_label = tkinter.Label(root, text='Hey there! I was clicked')
    text_label.pack()


def createFontColorButton(root, text):
    my_button = tkinter.Button(
        master=root,
        text=text,
        fg='red'
    )
    return my_button


def createBackgroundColorButton(root, text):
    my_button = tkinter.Button(
        master=root,
        text=text,
        bg='red'
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
        button.pack()

        disabled_button = createDiabledButton(
            root_button,
            'Click me if you can'
        )
        disabled_button.pack()

        padded_button = createPaddedButton(
            root_button,
            'Click here as well'
        )
        padded_button.pack()

        command_button = createCommandButton(
            root_button,
            'I execute a command'
        )
        command_button.pack()

        font_color_button = createFontColorButton(
            root_button,
            'I should have red text'
        )
        font_color_button.pack()

        background_color_button = createBackgroundColorButton(
            root_button,
            'I should be red'
        )
        background_color_button.pack()

        root_button.mainloop()


if __name__ == "__main__":
    main()
