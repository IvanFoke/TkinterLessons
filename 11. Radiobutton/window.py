from tkinter import *
from tkinter import messagebox as mb
from child_window import ChildWindow
from PIL import Image as PilImage
from PIL import ImageTk, ImageOps

RED = 0
ORANGE = 1
YELLOW = 2


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=r"resources/feather.ico"):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        img = PilImage.open(r"resources\face.png")
        neg = ImageOps.invert(img.convert("RGB"))
        img = img.resize((20, 20), PilImage.ANTIALIAS)
        neg = neg.resize((20, 20), PilImage.ANTIALIAS)
        self.smile = ImageTk.PhotoImage(img)
        self.neg_smile = ImageTk.PhotoImage(neg)

        self.choice = IntVar(value=1)
        self.info = Label(self.root)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        # Radiobutton(self.root, text="One", variable=self.choice, value=0, width=20, height=3, bg="green",
        #             fg="white").pack()
        # Radiobutton(self.root, text="Two", variable=self.choice, value=1, relief=SUNKEN, bd=5,
        #             image=self.smile, selectimage=self.neg_smile).pack()
        # Radiobutton(self.root, text="Looong text", variable=self.choice, value=2, font=("Verdana", 10),
        #             justify=CENTER, padx=5, pady=7, underline=1, wraplength=20).pack()
        # Radiobutton(self.root, text="active", variable=self.choice, value=4, selectcolor="red",
        #             activebackground="orange", activeforeground="yellow").pack()
        # Radiobutton(self.root, text="command", variable=self.choice, value=5).pack()

        # Radiobutton(self.root, text="red", variable=self.choice, value=RED, command=self.change_bg,
        #             indicatoron=0).pack()
        # Radiobutton(self.root, text="orange", variable=self.choice, value=ORANGE, command=self.change_bg,
        #             indicatoron=0).pack()
        # Radiobutton(self.root, text="yellow", variable=self.choice, value=YELLOW, command=self.change_bg,
        #             indicatoron=0).pack()

        Radiobutton(self.root, text="Sea", variable=self.choice, value=0, indicatoron=0, width=10,
                    command=lambda: self.show_info("sea")).pack(anchor=W)
        Radiobutton(self.root, text="Forest", variable=self.choice, value=1, indicatoron=0, width=10,
                    command=lambda: self.show_info("forest")).pack(anchor=W)
        Radiobutton(self.root, text="Jungle", variable=self.choice, value=2, indicatoron=0, width=10,
                    command=lambda: self.show_info("jungle")).pack(anchor=W)

        self.info.pack(anchor=CENTER)

        # Button(self.root, text="Save", width=10, command=self.command).pack()
        Button(self.root, text="Quit", width=10, command=self.exit).pack()

    def show_info(self, place):
        if place == "sea":
            self.info.configure(text="There are a lot of fishes", bg="blue", fg="white")
        elif place == "forest":
            self.info.configure(text="Here birds singing...", bg="green", fg="brown")
        else:
            self.info.configure(text="I don't know this place", bg="red", fg="blue")

    def change_bg(self):
        color = self.choice.get()
        if color == RED:
            self.root.configure(bg="red")
        elif color == ORANGE:
            self.root.configure(bg="orange")
        elif color == YELLOW:
            self.root.configure(bg="yellow")

    def command(self):
        choice = self.choice.get()
        mb.showinfo("Info", f"Choice = {choice}")

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

