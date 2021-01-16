import tkinter


def tkinterSetup():
    root = tkinter.Tk()
    return root


def createLabelFrame(root, text):
    my_label = tkinter.LabelFrame(
        master=root,
        text=text,
        padx=50,
        pady=50
    )
    return my_label


def createButton(frame, text):
    my_button = tkinter.Button(
        master=frame,
        text=text
    )
    return my_button


def main():

    running_status = {
        'frame': True
    }

    # FRAME
    if running_status['frame']:
        root = tkinterSetup()
        label_frame = createLabelFrame(root, 'It is a frame')
        label_frame.pack(padx=10, pady=10)
        button = createButton(label_frame, text='Hello there')
        button.pack()
        root.mainloop()


if __name__ == "__main__":
    main()
