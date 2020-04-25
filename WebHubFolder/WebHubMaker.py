from tkinter import *
import webbrowser

window = "null"

class window():
    def __init__(self, title, height, width):
        self.title = title
        self.height = height
        self.width = width

        global window

        window = Tk()

        window.title(self.title)

        if self.height == "auto" and self.width == "auto":
            return
        else:
            window.minsize(self.width, self.height)

class title():
    def __init__(self, text, font):
        self.text = text
        self.font = font

        label = Label(window, text=self.text, font=self.font + " 25" + " bold")

        label.pack()

class text():
    def __init__(self, text, font, size, fg, bg):
        self.text = text
        self.font = font
        self.size = size
        self.fg = fg
        self.bg = bg

        label = Label(window, text=self.text, font=self.font + " " + self.size, fg=self.fg, bg=self.bg)

        label.pack()

class link():
    def __init__(self, text, link, font, size):
        self.text = text
        self.link = link
        self.font = font
        self.size = size

        link = Label(window, text=self.text, font=self.font + " " + self.size, fg="blue", cursor="hand2")

        link.pack()

        link.bind("<Button-1>", lambda e:  webbrowser.open_new(self.link))

class dropdown():
    def __init__(self, items, default):
        self.items = items
        self.default = default

        var1 = StringVar()

        if default == "0":
            var1.set(items[0])
        else:
            var1.set(self.default)

        drop1 = OptionMenu(window, var1, *self.items, command=self.DDMG)
        drop1.pack()

    def DDMG(self, value):
        self.value = value

    def get(self):
        return self.value

class button():
    def __init__(self, text, height, width, command):
        self.text = text
        self.height = height
        self.width = width
        self.command = command

        button = Button(window, text=self.text, height=self.height, width=self.width, command=self.command)
        button.pack()

def start():
    window.mainloop()
