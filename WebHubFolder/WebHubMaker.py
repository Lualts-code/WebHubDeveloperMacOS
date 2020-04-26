from tkinter import *
import webbrowser

window = "null"

class window():
    def __init__(self, title, height, width, bg):
        self.title = title
        self.height = height
        self.width = width
        self.bg = bg

        global window

        window = Tk()

        window.title(self.title)

        window.configure(bg=self.bg)

        if self.height == "auto" and self.width == "auto":
            return
        else:
            window.minsize(self.width, self.height)

class title():
    def __init__(self, text, font, fg, bg):
        self.text = text
        self.font = font
        self.fg = fg
        self.bg = bg

        label = Label(window, text=self.text, font=self.font + " 25" + " bold", fg=self.fg, bg=self.bg)

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
    def __init__(self, text, link, font, size, bg):
        self.text = text
        self.link = link
        self.font = font
        self.size = size
        self.bg = bg

        link = Label(window, text=self.text, font=self.font + " " + self.size, fg="blue", cursor="hand2", bg=self.bg)

        link.pack()

        link.bind("<Button-1>", lambda e:  webbrowser.open_new(self.link))

class dropdown():
    def __init__(self, items, default, fg, bg):
        self.items = items
        self.default = default
        self.fg = fg
        self.bg = bg

        var1 = StringVar()

        if default == "0":
            var1.set(items[0])
        else:
            var1.set(self.default)

        drop1 = OptionMenu(window, var1, *self.items, command=self.DDMG)
        drop1.configure(fg=self.fg, bg=self.bg)
        drop1.pack()

    def DDMG(self, value):
        self.value = value

    def get(self):
        return self.value

class button():
    def __init__(self, text, height, width, command, fg, bg):
        self.text = text
        self.height = height
        self.width = width
        self.command = command
        self.fg = fg
        self.bg = bg

        button = Button(window, text=self.text, height=self.height, width=self.width, command=self.command, fg=self.fg, bg=self.bg)
        button.pack()

class input():
    def __init__(self, default, fg, bg):
        self.default = default
        self.fg = fg
        self.bg = bg

        global entry1

        entry1 = Entry(window, fg=self.fg, bg=self.bg)
        entry1.insert(0, self.default)
        entry1.pack()

    def get(self):
        return entry1.get()

def start():
    window.mainloop()
