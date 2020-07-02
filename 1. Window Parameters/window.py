from tkinter import *

window = Tk()

window.title("Экранное имя приложения")
window.geometry("800x600+200+200")

# Или так
# width = 800
# height = 600
# x = 200
# y = 200
# window.geometry(f"{width}x{height}+{x}+{y}")

window.resizable(False, False)

# Если иконка к приложению лежит в той же папке, что и .py код
window.iconbitmap("Имя иконки")

# Если нужен абсолютный путь к иконке
# window.iconbitmap(r"D:\путь\к\вашей\иконке\Имя иконки")

window.mainloop()
