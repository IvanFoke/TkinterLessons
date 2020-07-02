from tkinter import *
from child_window import ChildWindow


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=r"resources/feather.ico"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        # self.label = Label(self.root, text="I'm a label", bg="#e84ae5", relief=RIDGE, wraplength=40, font="Consolas 15")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        # top_frame = Frame(self.root, borderwidth=30, relief=SUNKEN, width=300, height=200)
        # bottom_frame = Frame(self.root, borderwidth=30, relief=SUNKEN, width=300, height=200)
        # top_frame.pack()
        # bottom_frame.pack()

        l1 = Label(self.root, width=300, height=20, bg='red', text="First")
        l2 = Label(self.root, width=30, height=2, bg='orange', text="Second")

        l1.place(x=10, y=10)
        l2.place(in_=l1, x=10, y=10)

        # Label(self.root, width=30, height=2, bg='red', text="First").place(relx=0.1, rely=0.5, relwidth=0.1, relheight=0.2)
        # Label(self.root, width=30, height=2, bg='orange', text="Second").place(x=100, y=100, width=100, height=50)
        # Label(top_frame, width=30, height=2, bg='yellow', text="Third").place(x=10, y=10, bordermode=OUTSIDE)
        # Label(bottom_frame, width=30, height=2, bg='green', text="Fourth").place(x=10, y=10, bordermode=INSIDE)
        # Label(self.root, width=30, height=2, bg='cyan', text="Fifth")

    def create_child(self, width, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    # window.create_child(200, 100)
    window.run()

