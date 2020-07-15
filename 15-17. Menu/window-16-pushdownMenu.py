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

        self.auto_save = BooleanVar(value=0)
        self.age = IntVar()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.draw_menu()
        Label(self.root, text="Just a label").pack()
        Button(self.root, text="Quit", width=10, command=self.exit).pack()

    def draw_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Сохранить", command=self.cmd)
        file_menu.add_command(label="Сохранить как...")
        file_menu.add_separator()
        file_menu.add_checkbutton(label="Автосохранение", offvalue=0, onvalue=1, variable=self.auto_save,
                                  command=self.auto_save_changed)
        file_menu.add_separator()
        file_menu.add_radiobutton(label="1 год", value=1, variable=self.age, command=self.age_changed)
        file_menu.add_radiobutton(label="2 года", value=2, variable=self.age, command=self.age_changed)
        file_menu.add_radiobutton(label="3 года", value=3, variable=self.age, command=self.age_changed)
        file_menu.add_separator()
        file_menu.add_command(label="Выйти", command=self.exit)

        menu_bar.add_cascade(label="Файл", menu=file_menu)
        self.root.configure(menu=menu_bar)

    def auto_save_changed(self):
        mb.showinfo("AutoSave", f"Value: {self.auto_save.get()}")

    def age_changed(self):
        mb.showinfo("Age", f"Value: {self.age.get()}")

    def cmd(self):
        mb.showinfo("123", "123")

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

