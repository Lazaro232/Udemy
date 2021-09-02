import tkinter as tk

from tkinter import ttk
from tkinter.constants import CENTER, END, NO, RIGHT, W, Y
from database import Database


# Initial Setup
root = tk.Tk()
root.title('HOME MÓVEIS PLANEJADOS')
root.geometry('1000x500')
notebook = ttk.Notebook(root)
notebook.pack(padx=5, pady=5)
database = Database()

# Style
style = ttk.Style()
# Theme
style.theme_use('default')
# Treeview colors
style.configure("Treeview",
                background='#D3D3D3', foreground='black',
                rowheight=25, fieldbackground='#D3D3D3')
# Change selected color
style.map('Treeview', background=[('selected', '#347083')])
# Treeview Frame
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)
# Scrollbar
tree_scroll = tk.Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
# Create the Treeview
tree = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
tree.pack()
# Configure Scrollbar
tree_scroll.config(command=tree.yview)
# Define Columns
tree['columns'] = ("ID", "Pessoa", "Nome", "CPF", "Email", "Contato")
# Format columns
tree.column("#0", width=0, stretch=NO)
tree.column("ID", anchor=CENTER, width=50)
tree.column("Pessoa", anchor=CENTER, width=60)
tree.column("Nome", anchor=W, width=300)
tree.column("CPF", anchor=W, width=130)
tree.column("Email", anchor=W, width=250)
tree.column("Contato", anchor=CENTER, width=150)
# Headings
tree.heading("#0", text="", anchor=W)
tree.heading("ID", text="ID", anchor=CENTER)
tree.heading("Pessoa", text="Pessoa", anchor=CENTER)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("CPF", text="CPF", anchor=W)
tree.heading("Email", text="Email", anchor=W)
tree.heading("Contato", text="Contato", anchor=CENTER)
# Row Tags
tree.tag_configure('oddrow', background="white")
tree.tag_configure('evenrow', background="lightblue")

# Add record Entry Boxes
data_frame = tk.LabelFrame(root, text="Dados do Cliente")
data_frame.pack(fill='x', expand=True, padx=20)

name_label = tk.Label(data_frame, text="Nome")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(data_frame)
name_entry.grid(row=0, column=1, padx=10, pady=10)

pessoa_label = tk.Label(data_frame, text="PF/PJ")
pessoa_label.grid(row=0, column=2, padx=10, pady=10)
pessoa_entry = tk.StringVar()
pessoa_entry.set("Física")  # Default value
pessoa_drop = tk.OptionMenu(data_frame, pessoa_entry, 'Física', 'Jurídica')
pessoa_drop.grid(row=0, column=3, padx=10, pady=10)

cpf_label = tk.Label(data_frame, text="CPF")
cpf_label.grid(row=0, column=4, padx=10, pady=10)
cpf_entry = tk.Entry(data_frame)
cpf_entry.grid(row=0, column=5, padx=10, pady=10)

email_label = tk.Label(data_frame, text="Email")
email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(data_frame)
email_entry.grid(row=1, column=1, padx=10, pady=10)

contato_label = tk.Label(data_frame, text="Contato")
contato_label.grid(row=1, column=2, padx=10, pady=10)
contato_entry = tk.Entry(data_frame)
contato_entry.grid(row=1, column=3, padx=10, pady=10)

id_label = tk.Label(data_frame, text="ID")
id_label.grid(row=1, column=4, padx=10, pady=10)
id_entry = tk.Entry(data_frame)
id_entry.grid(row=1, column=5, padx=10, pady=10)


def select_record(e):
    # Clear entry boxes
    clear_entries()
    # Grab record Number
    selected = tree.focus()
    # Grab record values
    values = tree.item(selected, 'values')
    # Print outputs
    id_entry.insert(0, values[0])
    pessoa_entry.insert(0, values[1])
    name_entry.insert(0, values[2])
    cpf_entry.insert(0, values[3])
    email_entry.insert(0, values[4])
    contato_entry.insert(0, values[5])


def clear_entries():
    # Clear entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    # pessoa_entry.delete(0, END)
    cpf_entry.delete(0, END)
    email_entry.delete(0, END)
    contato_entry.delete(0, END)


def remove_record():
    # Remove from database
    id, _, _, _, _, _ = get_entries()
    database.delete_client(id)
    # Remove from the Treeview
    x = tree.selection()[0]
    tree.delete(x)


def update_record():
    # Update the database
    id, pessoa, nome, cpf, email, contato = get_entries()
    database.update_client(id, pessoa, nome, cpf, email, contato)
    # Grab record number
    selected = tree.focus()
    # Update record in the Treeview
    tree.item(selected, text='',
              values=(id_entry.get(), pessoa_entry.get(), name_entry.get(),
                      cpf_entry.get(), email_entry.get(), contato_entry.get()))
    clear_entries()


def add_record():
    _, pessoa, nome, cpf, email, contato = get_entries()
    database.add_client(pessoa, nome, cpf, email, contato)
    # Clear entry boxes and Refresh the table
    refresh_table()


def query_database():
    records = database.query()
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            tree.insert(parent='', index='end', iid=count, text='',
                        values=(record[0], record[1], record[2],
                                record[3], record[4], record[5]),
                        tags=('evenrow', ))
        else:
            tree.insert(parent='', index='end', iid=count, text='',
                        values=(record[0], record[1], record[2],
                                record[3], record[4], record[5]),
                        tags=('oddrow', ))
        count += 1


def refresh_table():
    # Clear entries
    clear_entries()
    # Clear the Treeview Table
    tree.delete(*tree.get_children())  # row1, row2 ...
    # ReQueryTreeview table
    query_database()


def get_entries():
    id = id_entry.get()
    pessoa = pessoa_entry.get()
    nome = name_entry.get()
    cpf = cpf_entry.get()
    email = email_entry.get()
    contato = contato_entry.get()
    return id, pessoa, nome, cpf, email, contato


# Buttons and Dropdown Lists
button_frame = tk.LabelFrame(root, text="Comandos")
button_frame.pack(fill='x', expand=True, padx=20)

update_button = tk.Button(
    button_frame, text="Atualizar Cliente", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(
    button_frame, text="Adicionar Cliente", command=add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_button = tk.Button(
    button_frame, text="Remover Cliente", command=remove_record)
remove_button.grid(row=0, column=2, padx=10, pady=10)

search_button = tk.Button(
    button_frame, text="Pesquisar Cliente",)
search_button.grid(row=0, column=3, padx=10, pady=10)

clear_button = tk.Button(
    button_frame, text="Limpar Campos", command=clear_entries)
clear_button.grid(row=0, column=4, padx=10, pady=10)

update_table_button = tk.Button(
    button_frame, text="Atualizar Tabela", command=refresh_table)
update_table_button.grid(row=0, column=5, padx=10, pady=10)


# Bind Treeview
tree.bind("<ButtonRelease-1>", select_record)

# Run to pull data from database
query_database()

if __name__ == '__main__':
    root.mainloop()
