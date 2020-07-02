from tkinter import *
from child_window import ChildWindow


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=r"resources/feather.ico"):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.label = Label(self.root, text="I'm a label", bg="#e84ae5", relief=RIDGE, wraplength=40, font="Consolas 15")
        # .pgm, .ppm, .gif, .png
        # self.face_image = PhotoImage(file=r"resources/face.png")
        # self.label = Label(self.root, image=self.face_image)
        # self.label.image = self.face_image

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        top_frame = LabelFrame(self.root, text="Top frame")
        bottom_frame = LabelFrame(self.root, text="Bottom frame")
        top_frame.pack(padx=10, pady=10, expand=1, anchor=NW)
        bottom_frame.pack(ipadx=10, ipady=10, expand=1, fill=BOTH)

        # self.label.pack(anchor=NW, padx=100, pady=30)
        Label(top_frame, width=30, height=2, bg='red', text="First").pack(side=LEFT, padx=10)
        Label(top_frame, width=30, height=2, bg='orange', text="Second").pack(side=LEFT)
        Label(bottom_frame, width=30, height=2, bg='yellow', text="Third").pack(side=LEFT)
        Label(bottom_frame, width=30, height=2, bg='green', text="Fourth").pack(side=LEFT)
        Label(bottom_frame, width=30, height=2, bg='cyan', text="Fifth").pack(side=LEFT)

    def create_child(self, width, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    # window.create_child(200, 100)
    window.run()

