from tkinter import *
from tkinter import messagebox as mb
from child_window import ChildWindow


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=r"resources/feather.ico"):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.login_entry = Entry(self.root)
        self.age_entry = Entry(self.root)
        self.password_entry = Entry(self.root, show="*")

        # self.entry = Entry(self.root)
        # self.entry.insert(0, "Hey...")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, text="Login:", justify=LEFT).grid(row=0, column=0, sticky=W)
        self.login_entry.grid(row=0, column=1, sticky=W+E, padx=5, pady=5)
        Label(self.root, text="Age:", justify=LEFT).grid(row=1, column=0, sticky=W)
        self.age_entry.grid(row=1, column=1, sticky=W+E, padx=5, pady=5)
        Label(self.root, text="Password:", justify=LEFT).grid(row=2, column=0, sticky=W)
        self.password_entry.grid(row=2, column=1, sticky=W+E, padx=5, pady=5)

        # text_var = StringVar(value="Text")
        # Entry(self.root, width=30, fg="blue", font=("Verdana", 9), justify=CENTER, relief=SUNKEN, bd=3,
        #       selectbackground="green", selectforeground="yellow", textvariable=text_var).pack()

        # self.entry.pack()
        # Button(self.root, text="Show text", width=10, command=self.get_text).pack()
        # Button(self.root, text="Repeat", width=10, command=self.repeat_text).pack()
        # Button(self.root, text="Insert", width=10, command=self.insert).pack()
        # Button(self.root, text="Clear", width=10, command=self.clear).pack()

        Button(self.root, text="Save", width=10, command=self.save_data).grid(row=3, column=0, padx=5, sticky=E)
        Button(self.root, text="Quit", width=10, command=self.exit).grid(row=3, column=1, sticky=E)

    def exit(self):
        choice = mb.askyesno("Quit", "Do you want to quit?")
        if choice:
            self.root.destroy()

    def save_data(self):
        login = self.login_entry.get()
        age = int(self.age_entry.get())
        password = self.password_entry.get()

        mb.showinfo("User Data", f"Hello, {login}! You're {age} y.o.")

    # def get_text(self):
    #     text = self.entry.get()
    #     mb.showinfo("Entry text", text)
    #
    # def repeat_text(self):
    #     text = self.entry.get()
    #     self.entry.insert(0, text)
    #     self.entry.insert(END, text)
    #
    # def insert(self):
    #     self.entry.insert(INSERT, "_in_")
    #     self.entry.insert(ANCHOR, "_sel_")
    #
    # def clear(self):
    #     self.entry.delete(0, END)

    def button_action(self):
        Label(self.root, text="New label").pack()

    def create_child(self, width, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    # window.create_child(200, 100)
    window.run()

