import tkinter as tk
from tkinter import ttk


def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill='both', expand=True)

    notebook.add(text_area, text="Untitled")
    notebook.select(text_area)


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

file_menu = tk.Menu(menubar)
menubar.add_cascade(menu=file_menu, label="File")

file_menu.add_command(label="New", command=create_file)

notebook = ttk.Notebook(main)
notebook.pack(fill='both', expand=True)

create_file()
create_file()


root.mainloop()

'''
Anotaçoes:

1) root.config(menu=menubar)
Adiciona uma barra de menu principal

2) menubar.add_cascade(menu=file_menu, label="File")
Cria um campo dentro da barra de menu principal com o nome File e
esse campo é do tipo CASCADE (ou dropdown)

3) file_menu.add_command(label="New", command=create_file)
Adiciona um campo dentro de 'File' que executará um comando e
esse comando é a funçao create_file
'''
