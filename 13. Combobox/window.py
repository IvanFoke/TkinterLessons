from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
from child_window import ChildWindow
# from PIL import Image as PilImage
# from PIL import ImageTk, ImageOps


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=r"resources/feather.ico"):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.numbers = Combobox(self.root, values=(1, 3, 5), state="readonly")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.numbers.pack()
        Combobox(self.root, values=("one", "two", "three"), justify=CENTER).pack()

        self.numbers.bind("<<ComboboxSelected>>", self.changed)

        Button(self.root, text="Get", width=10, command=self.get_number).pack()
        Button(self.root, text="Quit", width=10, command=self.exit).pack()

    def changed(self, event):
        index = self.numbers.get()
        mb.showinfo("Info", f"Changed value, index: {index}")

    def get_number(self):
        value = self.numbers.get()
        index = self.numbers.current()

        mb.showinfo("Get info", f"Index: {index}, value: {value}")

    def exit(self):
        choice = mb.askyesno("Quit", "Do you want to quit?")
        if choice:
            self.root.destroy()

    def create_child(self, width, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    # window.create_child(200, 100)
    window.run()

