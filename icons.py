import tkinter


def tkinterSetup(title='Untitled', icon_path='images/icon.ico'):
    root = tkinter.Tk()
    root.title(title)
    root.iconbitmap(icon_path)
    return root


def createLabel(root, text):
    my_label = tkinter.Label(
        master=root,
        text=text
    )
    return my_label


def main():

    running_status = {
        'icon': True
    }

    # ICONS
    if running_status['icon']:
        root_icon = tkinterSetup(title='Icon Window')

        root_icon.mainloop()


if __name__ == "__main__":
    main()
