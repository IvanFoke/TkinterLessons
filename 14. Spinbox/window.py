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

        self.choice = StringVar()
        self.s = Spinbox(self.root, values=("One", "Two", "Three"))

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        # txt = StringVar(value="Text")
        # Spinbox(self.root, width=30, bg="black", fg="white", buttonbackground="yellow").pack()
        # Spinbox(self.root, relief=RAISED, bd=5, buttonuprelief=SUNKEN, buttondownrelief=RAISED).pack()
        # Spinbox(self.root, textvariable=txt, font=("Calibri", 12), justify=CENTER,
        #         selectbackground="blue", selectforeground="green").pack()

        # Spinbox(self.root, from_=2, to=10, increment=2).pack()
        # Spinbox(self.root, from_=2, to=10).pack()

        # Spinbox(self.root, values=(0, 1, 1, 2, 3, 5, 8)).pack()
        # Spinbox(self.root, values=("a", "b", "c"), state="readonly").pack()

        # Spinbox(self.root, values=("a", "b", "c"), textvariable=self.choice, state="readonly").pack()

        Spinbox(self.root, values=(1, 2, 3), state="readonly", textvariable=self.choice, command=self.my_command).pack()

        self.s.pack()

        Spinbox(self.root, from_=2, to=20, increment=5, wrap=True).pack()

        Button(self.root, text="Save", width=10, command=self.save).pack()
        Button(self.root, text="Quit", width=10, command=self.exit).pack()

    def my_command(self):
        choice = self.choice.get()
        mb.showinfo("Command", f"Got value {choice}")

    def save(self):
        # choice = self.choice.get()
        # mb.showinfo("Info", f"Got value {choice}")

        choice_1 = self.s.get()
        mb.showinfo("Info_1", f"Got value_1 {choice_1}")

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

