import tkinter as tk
from tkinter import messagebox

def name():
    name = entry.get()
    greeting_message = f"Привет, {name}!"
    messagebox.showinfo("Приветствие", greeting_message)

root = tk.Tk()

root.title("приветственная программа")

label = tk.Label(root, text="Введите свое имя")
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Ввести имя", command=name)
button.pack()

root.mainloop()
