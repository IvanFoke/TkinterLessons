from tkinter import *
from child_window import ChildWindow
from PIL import Image as PilImage
from PIL import ImageTk


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=r"resources/feather.ico"):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        img = PilImage.open(r"resources\face.png")
        img = img.resize((20, 20), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

        # self.label = Label(self.root, width=30, height=2, text="Unpressed", bg="green")
        self.label = Label(self.root, width=30, height=2, text="No color")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        # Button(self.root, width=30, height=5, text="Press me!", relief=GROOVE, bd=8).pack()
        # Button(self.root, width=30, text="New button", font=("Consolas", 10, "bold"), wraplength=15, justify=LEFT,
        #        underline=0).pack()
        # Button(self.root, text="image", image=self.photo_image, compound=LEFT).pack()
        # Button(self.root, text="Color", bg="green", fg="yellow",
        #        activebackground="yellow", activeforeground="green").pack()

        self.label.pack()

        Button(self.root, text="red", bg="red", width=20, command=lambda: self.change_color("red")).pack(anchor=W)
        Button(self.root, text="orange", bg="orange", width=20, command=lambda: self.change_color("orange")).pack(anchor=W)
        Button(self.root, text="yellow", bg="yellow", width=20, command=lambda: self.change_color("yellow")).pack(anchor=W)
        Button(self.root, text="green", bg="green", width=20, command=lambda: self.change_color("green")).pack(anchor=W)

        Button(self.root, text="Destroy", width=20, command=self.root.destroy).pack(anchor=E)
        Button(self.root, text="Quit", width=20, command=quit).pack(anchor=E)

        # Button(self.root, text="Press me", command=self.change_label).pack()
        # Button(self.root, text="Create label", command=self.button_action).pack()

        # str_var = StringVar(value="str var!")
        # Button(self.root, width=30, height=5, textvariable=str_var).pack()

    def change_color(self, color):
        self.label.configure(text=color, fg=color)
        self.root.configure(bg=color)

    def change_label(self):
        self.label.configure(text="Pressed", bg="red")

    def button_action(self):
        Label(self.root, text="New label").pack()

    def create_child(self, width, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    # window.create_child(200, 100)
    window.run()

