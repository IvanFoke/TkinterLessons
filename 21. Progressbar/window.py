from tkinter import *
from tkinter import messagebox as mb
# from tkinter.scrolledtext import ScrolledText
# from tkinter import filedialog as fd
from tkinter.ttk import Progressbar
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

        self.pb = Progressbar(self.root, orient=HORIZONTAL, mode="indeterminate", length=200)
        self.sb = Spinbox(self.root, from_=0, to=100, state='readonly', command=self.change_pb)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.draw_menu()
        self.sb.pack()
        self.pb.pack()
        # self.pb.configure(maximum=3)
        # self.pb.configure(value=1)

        # from time import sleep
        # for i in range(101):
        #     self.pb.configure(value=i)
        #     self.pb.update()
        #     sleep(0.05)
        # self.pb.configure(value=0)

        Button(self.root, text="StartPB", command=self.pb.start).pack()
        Button(self.root, text="StopPB", command=self.pb.stop).pack()

        value = self.pb["value"]
        self.pb["value"] = 20

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

    def change_pb(self):
        self.pb.configure(value=self.sb.get())
        self.pb.update()

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

