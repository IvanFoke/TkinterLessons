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
        self.root.geometry("+600+300")
        # self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.auto_save = BooleanVar(value=0)
        self.age = IntVar()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.draw_menu()
        Label(self.root, text="Just a label").pack()
        Button(self.root, text="Quit", width=10, command=self.exit).pack()

    def draw_menu(self):
        menu_bar = Menu(self.root)
		
		menu_bar.add_command(label="Hey", command=self.cmd)
		menu_bar.add_command(label="Edit")
		menu_bar.add_command(label="Help")
        
        self.root.configure(menu=menu_bar)

    def cmd(self):
        mb.showinfo("123", "123")

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

