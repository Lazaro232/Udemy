import os
import tkinter as tk
from tkinter import ttk, filedialog


def create_file(content="", title="Untitled"):
    text_area = tk.Text(notebook)
    text_area.insert("end", content)
    text_area.pack(fill='both', expand=True)
    notebook.add(text_area, text=title)
    notebook.select(text_area)


def save_file():
    file_path = filedialog.asksaveasfilename()

    try:
        filename = os.path.basename(file_path)
        text_widget = root.nametowidget(notebook.select())
        content = text_widget.get("1.0", "end-1c")

        with open(file_path, "w") as file:
            file.write(content)

    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return

    notebook.tab("current", text=filename)


def open_file():
    file_path = filedialog.askopenfilename()

    try:
        filename = os.path.basename(file_path)
        with open(file_path, "r") as file:
            content = file.read()
    except (AttributeError, FileNotFoundError):
        print("Open operation cancelled")
        return

    create_file(content, filename)


# Instanciando o objeto Tkinter
root = tk.Tk()
root.title("My Text Editor")
root.option_add("*tearOff", False)
# Definindo um 'main frame'
main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True, padx=10, pady=(4, 0))
# Menu bar
menubar = tk.Menu()
root.config(menu=menubar)
# File dropdown
file_menu = tk.Menu(menubar)
menubar.add_cascade(menu=file_menu, label="File")
file_menu.add_command(label="New", command=create_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open...", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")


notebook = ttk.Notebook(main)
notebook.pack(fill='both', expand=True)

create_file()

root.bind("<Control-n>", lambda event: create_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())


root.mainloop()

'''
Anotaçoes:

1) accelerator= ...
Adiciona um atalho para o comando

2) .bind
recebe o comando do teclado + a funcao que irá executar

'''
