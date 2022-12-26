import tkinter.messagebox
from tkinter import *


class Flashlight:
    def __init__(self, connetion):
        self.root = Tk()
        self.background_color = "#FFFFFF"
        self.root['bg'] = '#323232'
        self.root.geometry('606x606')
        self.root.resizable(False, False)
        self.c = Canvas(self.root, width=600, height=550, bg="#000000", bd=0)
        self.c.grid(row=0, column=0)
        self.root.bind("<<on_event>>", self.on)
        self.root.bind("<<off_event>>", self.off)

        self.connection = connetion

    def on(self):
        self.c.configure(bg=self.background_color)

    def off(self):
        self.c.configure(bg="#000000")

    def color(self, color):
        self.background_color = "#" + color
        self.c.configure(bg=self.background_color)

    def on_closing(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.connection.close()
            self.root.destroy()


    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
