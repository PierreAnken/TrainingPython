import tkinter
if __name__ == '__main__':

    #  create the base windows
    window = tkinter.Tk()
    window.title('Some title')
    window.geometry('300x100')

    # create the close button
    close_button = tkinter.Button(
        master=window,
        text="Close",
        command=window.quit
    )

    # add it to the window
    close_button.pack(padx=50, pady=50)

    # hear for events
    window.mainloop()
