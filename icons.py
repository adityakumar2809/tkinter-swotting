import tkinter


def tkinterSetup(title='Untitled'):
    root = tkinter.Tk()
    root.title(title)
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
        pass


if __name__ == "__main__":
    main()
