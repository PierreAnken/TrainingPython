import os
import tkinter

import openai as openai

openai.api_key = os.environ['GPT_KEY']


def ask_gpt(prompt: tkinter.StringVar, destination_label: tkinter.StringVar):
    response = openai.Completion.create(
        model="text-davinci-001",
        prompt=prompt.get(),
        temperature=0.3,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    text_area.insert(tkinter.END, response['choices'][0]['text'])


#  create the base windows
window = tkinter.Tk()
window.title('Chat GPT')
window.geometry('800x600')

# create the close button
close_button = tkinter.Button(
    master=window,
    text="Close",
    command=window.quit
)

# add it to the window
close_button.pack(padx=50, pady=50)

# Prompt
text_value = tkinter.StringVar()
entree = tkinter.Entry(
    master=window,
    textvariable=text_value,
    width=30
)
entree.pack(pady=10, padx=20)

# Response

text_area = tkinter.Text(
    master=window,
)
text_area.config(width=100, height=20)
text_area.pack()

# Send button
send_button = tkinter.Button(
    master=window,
    text="Send",
    command=lambda: ask_gpt(text_value, text_area)
)
send_button.pack(pady=10)

# hear for events
window.mainloop()
