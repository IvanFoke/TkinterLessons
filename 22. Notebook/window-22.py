from tkinter import *
from tkinter import messagebox as mb
# from tkinter.scrolledtext import ScrolledText
# from tkinter import filedialog as fd
from tkinter.ttk import Notebook
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

        self.tabs_control = Notebook(self.root, height=100, width=30, padding=(10, 20, 30, 40))
        self.tabs_control.enable_traversal()
        self.tab_1 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_1, text="First tab", underline=0)

        self.tab_2 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_2, text="Second tab", underline=1)

        self.tabs_control.bind("<<NotebookTabChanged>>", self.tab_changed)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.draw_menu()
        self.tabs_control.pack(fill=BOTH, expand=1)

        Label(self.tab_1, text="Hello on the fist tab!", height=5, bg="green").pack()
        Text(self.tab_2).pack()

        # self.tabs_control.forget(self.tab_2)
        # self.tabs_control.forget(1)

        tab_3 = Frame(self.tabs_control)
        # self.tabs_control.insert(END, tab_3, text="Third tab")
        self.tabs_control.insert("end", tab_3, text="Third tab")

        tab_4 = Frame(self.tabs_control)
        self.tabs_control.insert(2, tab_4, text="Fourth tab")

        self.tabs_control.select(tab_3)
        print(f"Selected tab: {self.tabs_control.select()}")

        print(f"tab_4 params: {self.tabs_control.tab(tab_4)}")
        print(f"tab_4 params: {self.tabs_control.tab(tab_4, 'sticky')}")
        self.tabs_control.tab(tab_4, text="4th tab", underline=1)
        print(f"tab_4 params: {self.tabs_control.tab(tab_4)}")

        print(f"Managed tabs: {self.tabs_control.tabs()}")

        print(f"Params: {self.tabs_control.tab(0)}")
        print(f"Params: {self.tabs_control.tab('current')}")
        # print(f"Params: {self.tabs_control.tab(CURRENT)}")
        print(f"Params: {self.tabs_control.tab(self.tab_2)}")

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

    def tab_changed(self, event):
        print(f"Changed tab to: {self.tabs_control.select()}")

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
