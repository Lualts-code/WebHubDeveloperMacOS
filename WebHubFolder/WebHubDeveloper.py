from tkinter import *
import os

def open():
    os.system("python projects/" + entry.get() + ".py")

window = Tk()
window.title("WebHubDeveloper")
window.minsize(250, 50)

entry = Entry(window)
entry.insert(0, "Name of your Web.")

button = Button(window, text="Open", command=open)

entry.pack()
button.pack()

window.mainloop()
