import tkinter


def tkinterSetup():
    root = tkinter.Tk()
    return root


def createBlankEntry(root):
    entry = tkinter.Entry(root)
    return entry


def createWideEntry(root):
    entry = tkinter.Entry(root, width=60)
    return entry


def createFontColorEntry(root):
    entry = tkinter.Entry(root, fg='green')
    return entry


def createBackgroundColorEntry(root):
    entry = tkinter.Entry(root, bg='blue')
    return entry


def createCommandButton(root, text, entry):
    my_button = tkinter.Button(
        master=root,
        text=text,
        command=lambda: showLabelOnClick(root, entry)
    )
    return my_button


def showLabelOnClick(root, entry):
    text_label = tkinter.Label(root, text=entry.get())
    text_label.pack()


def main():

    running_status = {
        'input': True
    }

    # INPUT
    if running_status['input']:
        root_input = tkinterSetup()
        blank_entry = createBlankEntry(root_input)
        blank_entry.pack()

        wide_entry = createWideEntry(root_input)
        wide_entry.pack()

        font_color_entry = createFontColorEntry(root_input)
        font_color_entry.pack()

        background_color_entry = createBackgroundColorEntry(root_input)
        background_color_entry.pack()

        text_entry = createBlankEntry(root_input)
        text_entry.pack()

        button = createCommandButton(
            root_input,
            'Click here to submit',
            text_entry
        )
        button.pack()

        root_input.mainloop()


if __name__ == "__main__":
    main()
