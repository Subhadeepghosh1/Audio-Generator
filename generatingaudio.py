import os
from gtts import gTTS
from tkinter import *


root = Tk()
canvas = Canvas(root,width=400,height=300)
canvas.pack()

def text():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text,lang =language,slow = False)
    output.save('output.mp3')
    os.system("start output.mp3")

entry = Entry(root)
canvas.create_window(200,180,window = entry)

button = Button(text="Start",command=text)
canvas.create_window(200,230,window = button)




root.mainloop()
