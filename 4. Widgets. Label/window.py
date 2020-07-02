from tkinter import *
from child_window import ChildWindow


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=r"resources/feather.ico"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
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
        self.label.pack(anchor=NW, padx=100, pady=30)

    def create_child(self, width, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    # window.create_child(200, 100)
    window.run()

