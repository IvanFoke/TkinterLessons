from tkinter import *
from tkinter import messagebox as mb
from tkinter.scrolledtext import ScrolledText
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

        self.st = ScrolledText(self.root, width=50, height=5, bg="yellow", fg="green", relief=SUNKEN, bd=8,
                               selectbackground="red", selectforeground="blue", font=("Arial", 11, "bold"),
                               padx=5, pady=8, wrap=WORD, spacing1=10, spacing2=20, spacing3=30, tabs=300,
                               state=DISABLED)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.draw_menu()

        self.st.configure(state=NORMAL)

        self.st.tag_config("ref", background="blue", foreground="white", underline=1, font=("Consolas", 14),
                           justify=CENTER, offset=-8, relief=RAISED, borderwidth=2)

        # self.st.insert("1.0", "My\ntext\n1234")
        # self.st.insert("2.1", "Hello")
        self.st.insert("1.0", "SomeText " * 7)
        self.st.insert("1.8", "\n")

        self.st.tag_add("ref", "1.2", "1.10")
        self.st.insert(END, "REFERENCE", "ref")

        self.st.delete("1.3", "1.6")
        print(self.st.get("2.2", "2.5"))

        self.st.see("1.0")
        # self.st.search()

        # Indices
        # "1.2"
        # "2.end"
        # INSERT
        # CURRENT
        # END
        # "tag.first", "tag.end" ("ref.start")
        # "+ n chars" "- 1 chars"
        # "+ n lines" "- 2 lines"
        # "linestart", "lineend"
        # "wordstart", "wordend"
        # "+ 3 chars" => "+3c", "- 2 lines" => "-2l"
        index = "1.0"
        index += "+1c"

        self.st.configure(state=DISABLED)

        self.st.pack()

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

