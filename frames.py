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


def main():

    running_status = {
        'frame': True
    }

    # FRAME
    if running_status['frame']:
        root = tkinterSetup()
        text_label_frame = createLabelFrame(root, 'It is a frame')
        text_label_frame.pack(padx=10, pady=10)
        root.mainloop()


if __name__ == "__main__":
    main()
