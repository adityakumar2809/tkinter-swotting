import tkinter


def tkinterSetup():
    root = tkinter.Tk()
    return root


def main():

    running_status = {
        'input': True
    }

    # INPUT
    if running_status['input']:
        root_input = tkinterSetup()

        root_input.mainloop()


if __name__ == "__main__":
    main()
