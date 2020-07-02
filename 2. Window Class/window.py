from tkinter import *


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    window = Window(300, 300)
    window.run()
