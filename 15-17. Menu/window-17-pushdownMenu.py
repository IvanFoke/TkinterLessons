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
        self.auto_load = BooleanVar(value=0)
        self.value = IntVar()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.draw_menu()
        Label(self.root, text="Just a label").pack()

    def draw_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Сохранить", command=self.cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Выйти", command=self.exit)

        edit_menu = Menu(menu_bar, tearoff=0)
        parameters_menu = Menu(edit_menu, tearoff=0)
        parameters_menu.add_checkbutton(label="Автосохранение", offvalue=0, onvalue=1, variable=self.auto_save)
        parameters_menu.add_checkbutton(label="Автозагрузка", offvalue=0, onvalue=1, variable=self.auto_load,
                                        command=self.check_auto_load)
        edit_menu.add_cascade(label="Параметры", menu=parameters_menu)
        edit_menu.add_separator()

        values_menu = Menu(edit_menu, tearoff=0)
        values_menu.add_radiobutton(label="Один", value=1, variable=self.value)
        values_menu.add_radiobutton(label="Два", value=2, variable=self.value)
        values_menu.add_radiobutton(label="Три", value=3, variable=self.value)
        edit_menu.add_cascade(label="Значения", menu=values_menu)

        info_menu = Menu(menu_bar, tearoff=0)
        info_menu.add_command(label="О приложении", command=self.show_info)

        menu_bar.add_cascade(label="Файл", menu=file_menu)
        menu_bar.add_cascade(label="Настройки", menu=edit_menu)
        menu_bar.add_cascade(label="Справка", menu=info_menu)
        self.root.configure(menu=menu_bar)

    def check_auto_load(self):
        if not self.auto_save.get() and self.auto_load.get():
            if mb.askyesno("Ошибка", "Автозагрузка без автосохранения. Хотите установить автосохранение?"):
                self.auto_save.set(True)

    def show_info(self):
        mb.showinfo("Информация", "Лучшее графическое приложение на свете")

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

