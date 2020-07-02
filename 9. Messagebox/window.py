from tkinter import *
from tkinter import messagebox
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
        Button(self.root, text="info", width=10, command=lambda: messagebox.showinfo("Info", "Info message")).pack()
        Button(self.root, text="warning", width=10, command=lambda: messagebox.showwarning("Warning", "Warning message")).pack()
        Button(self.root, text="error", width=10, command=lambda: messagebox.showerror("Error", "Error message")).pack()

        Button(self.root, text="quit", width=10, command=self.exit).pack()

    def exit(self):
        choice = messagebox.askyesno("Quit", "Do you want to quit?")
        if choice:
            self.root.destroy()

    def button_action(self):
        Label(self.root, text="New label").pack()

    def create_child(self, width, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    # window.create_child(200, 100)
    window.run()

