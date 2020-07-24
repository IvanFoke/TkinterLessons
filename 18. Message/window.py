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
        self.root.geometry("+600+300")
        # self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.txt = StringVar(value="Hey")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.draw_menu()
        Message(self.root, text="My Message", bg="red", fg="white", font=("Verdana", 8, "italic"), justify=CENTER).pack()
        Message(self.root, text="My\nMessage\n1", relief=RAISED, bd=3, width=100, padx=20, pady=30).pack()
        Message(self.root, textvariable=self.txt).pack()

        self.txt.set("Hey123")
        print(self.txt.get())

    def draw_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_separator()
        file_menu.add_command(label="Выйти", command=self.exit)

        info_menu = Menu(menu_bar, tearoff=0)
        info_menu.add_command(label="О приложении", command=self.show_info)

        menu_bar.add_cascade(label="Файл", menu=file_menu)
        menu_bar.add_cascade(label="Справка", menu=info_menu)
        self.root.configure(menu=menu_bar)

    def show_info(self):
        mb.showinfo("Информация", "Лучшее графическое приложение на свете")

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

