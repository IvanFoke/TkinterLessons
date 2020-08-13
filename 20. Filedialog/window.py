from tkinter import *
from tkinter import messagebox as mb
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd
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

        self.text = ScrolledText(self.root)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.draw_menu()
        self.text.pack()

    def draw_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Открыть", command=self.open_file)
        file_menu.add_command(label="Сохранить как", command=self.save_file)
        file_menu.add_command(label="Отркыть папку", command=self.open_dir)
        file_menu.add_separator()
        file_menu.add_command(label="Выйти", command=self.exit)

        info_menu = Menu(menu_bar, tearoff=0)
        info_menu.add_command(label="О приложении", command=self.show_info)

        menu_bar.add_cascade(label="Файл", menu=file_menu)
        menu_bar.add_cascade(label="Справка", menu=info_menu)
        self.root.configure(menu=menu_bar)

    def open_file(self):
        # wanted_files = (
        #     ("IMAGES", "*.jpeg;*.png;*.gif"),
        #     ("TEXT files", "*.txt;*.log"),
        #     ("PY files", "*.py"),
        #     ("ALL", "*.*")
        # )
        #
        # file_name = fd.askopenfilename(initialdir="D:/", title="FIND A FILE", filetypes=wanted_files)
        # self.text.insert(END, f"Надо открыть файл: {file_name}\nСодержимое:\n")
        # if file_name:
        #     with open(file_name, "r") as f:
        #         self.text.insert(END, f.read())

        # file = fd.askopenfile()
        # self.text.insert(END, file.read())
        # file.close()

        file_names = fd.askopenfilenames()
        self.text.insert(END, str(file_names))

    def save_file(self):
        name = fd.asksaveasfilename(filetypes=(("TEXT files", "*.txt"), ("Py files", "*.py")))
        if name:
            self.text.insert(END, f"Сохранить файл по пути {name}\n")
            # with open(name, "w") as f:
            #     f.write("123")

        # file = fd.asksaveasfile()
        # file.write("123")
        # file.close()

    def open_dir(self):
        path = fd.askdirectory(mustexist=True)
        self.text.insert(END, f"Папка {path}\n")

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

