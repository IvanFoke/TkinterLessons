from tkinter import *
from tkinter import messagebox as mb
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

        # img = PilImage.open(r"resources\face.png")
        # neg = ImageOps.invert(img.convert("RGB"))
        # img = img.resize((20, 20), PilImage.ANTIALIAS)
        # neg = neg.resize((20, 20), PilImage.ANTIALIAS)
        # self.smile = ImageTk.PhotoImage(img)
        # self.neg_smile = ImageTk.PhotoImage(neg)

        self.parameters = (("red", IntVar()), ("orange", IntVar()), ("yellow", IntVar()))

        self.milk_var = IntVar()
        self.bread_var = IntVar()

        self.c = Checkbutton(self.root)
        self.c.invoke()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        # Checkbutton(self.root, text="Choice", bg="yellow", fg="green", activebackground="green",
        #             activeforeground="yellow", selectcolor="blue").pack()
        # Checkbutton(self.root, text="Another choice", width=15, height=3, relief=SUNKEN, bd=5).pack()
        # Checkbutton(self.root, image=self.smile, selectimage=self.neg_smile).pack()
        # Checkbutton(self.root, text="SomeText", font=("Courier", 10), justify=CENTER, underline=2, wraplength=20).pack()

        # Label(self.root, text="Shopping bag").pack()
        # Checkbutton(self.root, text="Milk", variable=self.milk_var).pack()
        # Checkbutton(self.root, text="Bread", variable=self.bread_var).pack()

        for name, var in self.parameters:
            Checkbutton(self.root, text=name, variable=var).pack()

        Checkbutton(self.root, text="command", command=self.change_state).pack()

        Checkbutton(self.root, text="Btn1", indicatoron=0).pack()
        Checkbutton(self.root, text="Btn2", indicatoron=0).pack()

        Button(self.root, text="Save", width=10, command=self.show_parameters).pack()
        # Button(self.root, text="Check", width=10, command=self.check_bag).pack()
        Button(self.root, text="Quit", width=10, command=self.exit).pack()

    def change_state(self):
        mb.showinfo("Command", "Checkbutton command changed state")

    def show_parameters(self):
        state = ("inactive", "active")
        text = ""

        for name, var in self.parameters:
            text += f"{name} is {state[var.get()]}\n"
        mb.showinfo("Parameters", text)


    def check_bag(self):
        text = ""
        if self.milk_var.get():
            text += "You've bought milk\n"
        else:
            text += "You need to buy milk\n"
        if self.bread_var.get():
            text += "You've bought bread\n"
        else:
            text += "You need to buy bread\n"
        mb.showinfo("Bag", text)

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

