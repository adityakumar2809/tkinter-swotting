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
        'basic': False,
        'grid': True
    }

    # BASIC
    if running_status['basic']:
        root_basic = tkinterSetup()
        text_label = createLabel(root_basic, 'Hello World!')
        text_label.pack()
        root_basic.mainloop()

    # GRID
    if running_status['grid']:
        root_grid = tkinterSetup()
        text_label_1 = createLabel(root_grid, 'Hello World!')
        text_label_2 = createLabel(root_grid, 'I am Aditya')
        text_label_1.grid(row=0, column=0)
        text_label_2.grid(row=1, column=1)
        root_grid.mainloop()


if __name__ == "__main__":
    main()
