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

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        l1 = Label(self.root, width=30, height=2, bg='orange', text="Second")
        l2 = Label(self.root, width=30, height=2, bg='yellow', text="Third")
        l3 = Label(self.root, width=30, height=2, bg='green', text="Fourth")

        l1.grid(row=0, column=0)
        l2.grid(row=0, column=1)
        l3.grid(row=1, column=0, columnspan=2)
        Label(self.root, width=30, height=2, bg='red', text="First").grid(row=2, column=0)

        # l1.grid_remove()
        # l1.grid_forget()
        # l1.grid()

        print(l1.grid_info())
        print(self.root.grid_size())
        print(self.root.grid_location(x=20, y=50))

        # Label(self.root, width=30, height=2, bg='red', text="First").grid(row=0, column=0, rowspan=2, sticky=S+N)
        # Label(self.root, width=30, height=2, bg='orange', text="Second").grid(row=0, column=0, padx=10)
        # Label(self.root, width=30, height=2, bg='yellow', text="Third").grid(row=0, column=1, pady=20)
        # Label(self.root, width=30, height=2, bg='green', text="Fourth").grid(row=1, column=1)
        # Label(self.root, width=30, height=2, bg='cyan', text="Fifth").grid(row=1, column=0, columnspan=2, sticky=W+E)

    def create_child(self, width, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    # window.create_child(200, 100)
    window.run()

