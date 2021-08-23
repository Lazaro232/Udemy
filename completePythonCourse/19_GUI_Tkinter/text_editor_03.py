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
file_menu.add_command(label="New", command=create_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)


notebook = ttk.Notebook(main)
notebook.pack(fill='both', expand=True)

create_file()


root.mainloop()

'''
Anotaçoes:

1) file_path = filedialog.asksaveasfilename()
Pergunta ao usuário onde ele quer salvar o arquivo. Faz isso usando
o diálogo nativo do sistema operacional utilizado

1.1 --> NAO SALVA O ARQUIVO, APENAS PERGUNTA ONDE

2) filename = os.path.basename(file_path)
Recupera o caminho do arquivo

3) content = text_widget.get("1.0", "end-1c")
1.0 --> 1 = Primeira linha. 0 = primeiro caractere
end-1c --> Até o final do conteúdo exceto o útimo caractere

Isso retorna todo o conteúdo escrito

4) with open(file_path, "w") as file:
       file.write(content)
Salva o arquivo no sistema

5) notebook.tab("current", text=filename)
Muda o nome da aba atualmente selecionada ("current") para
o nome escolhido do arquivo (filename)

6) text_area.insert("end", content)
Adiciona o conteúdo no final do arquivo (aba) (no caso de uma aba nova
o final será o começo)

'''
