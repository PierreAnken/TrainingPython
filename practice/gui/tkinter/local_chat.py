import datetime
import tkinter

if __name__ == '__main__':
    #  create the root and separate windows
    root = tkinter.Tk()
    window = tkinter.Toplevel(root)
    window2 = tkinter.Toplevel(root)

    window.title('Window 1')
    window2.title('Window 2')

    # hide root window
    root.withdraw()

    # add the inputs
    text_value = tkinter.StringVar()
    entree = tkinter.Entry(
        master=window,
        textvariable=text_value,
        width=30
    )
    entree.pack(pady=10, padx=20)

    text_value2 = tkinter.StringVar()
    entree2 = tkinter.Entry(
        master=window2,
        textvariable=text_value2,
        width=30
    )
    entree2.pack(pady=10, padx=20)


    def send_message(source_text: tkinter.StringVar, destination_label: tkinter.StringVar):
        current_text = destination_label.get()
        if 'No message' in current_text:
            current_text = ''

        current_time = str(datetime.datetime.now())[:16]
        text_to_add = f'\n{current_time} > {source_text.get()}'
        destination_label.set(current_text + text_to_add)

    # add the labels
    label_var = tkinter.StringVar()
    label_var.set('No message')
    label = tkinter.Label(
        master=window,
        textvariable=label_var
    )
    label.config(width=100, height=10)
    label.pack()

    label_var2 = tkinter.StringVar()
    label_var2.set('No message')
    label2 = tkinter.Label(
        master=window2,
        textvariable=label_var2,
    )
    label2.config(width=100, height=10)
    label2.pack()

    # add the send button
    send_button = tkinter.Button(
        master=window,
        text="Send",
        command=lambda: send_message(text_value, label_var2)
    )
    send_button.pack(pady=10)

    send_button2 = tkinter.Button(
        master=window2,
        text="Send",
        command=lambda: send_message(text_value2, label_var)
    )
    send_button2.pack(pady=10)

    # listen for events
    root.mainloop()
