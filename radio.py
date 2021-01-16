import tkinter


global radio_variable, value_label


def tkinterSetup():
    root = tkinter.Tk()
    return root


def createRadioButton(root, text, value):
    my_radio = tkinter.Radiobutton(
        master=root,
        text=text,
        variable=radio_variable,
        value=value,
        command=lambda: updateLabelValue(radio_variable.get())
    )
    return my_radio


def createLabel(root, text):
    my_label = tkinter.Label(
        master=root,
        text=text
    )
    return my_label


def updateLabelValue(value):
    global value_label
    value_label.config(text=f'Value is {value}')


def main():

    global radio_variable, value_label

    running_status = {
        'radio_button': True
    }

    # RADIO BUTTON
    if running_status['radio_button']:
        root = tkinterSetup()

        radio_variable = tkinter.IntVar()

        radio_1 = createRadioButton(root, 'Option 1', 1)
        radio_2 = createRadioButton(root, 'Option 2', 2)
        radio_3 = createRadioButton(root, 'Option 3', 3)
        radio_1.pack()
        radio_2.pack()
        radio_3.pack()

        value_label = createLabel(
            root,
            f'Value is {radio_variable.get()}'
        )
        value_label.pack()
        root.mainloop()


if __name__ == "__main__":
    main()
