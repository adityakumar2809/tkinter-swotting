import tkinter


global radio_variable


def tkinterSetup():
    root = tkinter.Tk()
    return root


def createRadioButton(root, text, value):
    my_radio = tkinter.Radiobutton(
        master=root,
        text=text,
        variable=radio_variable,
        value=value
    )
    return my_radio


def main():

    global radio_variable

    running_status = {
        'radio_button': True
    }

    # RADIO BUTTON
    if running_status['radio_button']:
        root = tkinterSetup()
        radio_variable = tkinter.IntVar()
        # radio_variable.get()
        radio_1 = createRadioButton(root, 'Option 1', 1)
        radio_2 = createRadioButton(root, 'Option 2', 2)
        radio_3 = createRadioButton(root, 'Option 3', 3)
        radio_1.pack()
        radio_2.pack()
        radio_3.pack()
        root.mainloop()


if __name__ == "__main__":
    main()
