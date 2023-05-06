import tkinter
from tkinter.messagebox import showinfo

if __name__ == '__main__':
    #  create the base windows
    window = tkinter.Tk()
    window.title('Some title')
    window.geometry('300x100')

    # create the input and add it
    text_value = tkinter.StringVar()
    entree = tkinter.Entry(
        master=window,
        textvariable=text_value,
        width=30
    )
    entree.pack(pady=10, padx=20)

    # function to call when clicking the alert button
    def show_alert():
        showinfo(message=text_value.get())

    # create the alert button and add it to the window
    alert_button = tkinter.Button(
        master=window,
        text="Alert",
        command=show_alert
    )
    alert_button.pack(pady=10)

    # listen for events
    window.mainloop()
