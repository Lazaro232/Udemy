import tkinter as tk
from tkinter import ttk


def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill='both', expand=True)

    notebook.add(text_area, text="Untitled")
    notebook.select(text_area)


# Instanciando o objeto Tkinter
root = tk.Tk()
# Definindo um 'main frame'
main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True, padx=10, pady=(4, 0))

notebook = ttk.Notebook(main)
notebook.pack(fill='both', expand=True)

create_file()
create_file()


root.mainloop()

'''
Anotaçoes:

1) .Text()
Se difere do .Entry pelo fato de ter mais espaço. Ou seja, é multi linha

2) notebook.select(text_area)
Garante que ao criar uma nova aba, a nova aba seja selecionada automaticamente
'''
