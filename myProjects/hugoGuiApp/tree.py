import tkinter as tk
import difflib

from tkinter import ttk
from tkinter.constants import BOTTOM, CENTER, END, NO, RIGHT, W, X, Y
from database import Database

ESTADOS = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
    'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]

# Initial Setup
root = tk.Tk()
root.title('HOME MÓVEIS PLANEJADOS')
root.geometry('1100x600')
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
# Vertical Scrollbar
y_scroll = tk.Scrollbar(tree_frame)
y_scroll.pack(side=RIGHT, fill=Y)
# Horizontal Scrollbar
x_scroll = tk.Scrollbar(tree_frame, orient='horizontal')
x_scroll.pack(side=BOTTOM, fill=X)
# Create the Treeview
tree = ttk.Treeview(
    tree_frame, xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set,
    selectmode="extended")
tree.pack()
# Configure Scrollbars
y_scroll.config(command=tree.yview)
x_scroll.config(command=tree.xview)

# Define Columns
tree['columns'] = ("ID", "Nome", "CPF", "Email", "Contato", "Pessoa",
                   "RG", "Estado", "Endereço", "Cidade", "Bairro", "CEP")
# Format columns
tree.column("#0", width=0, stretch=NO)
tree.column("ID", anchor=CENTER, width=50)
tree.column("Nome", anchor=CENTER, width=300)
tree.column("CPF", anchor=CENTER, width=130)
tree.column("Email", anchor=CENTER, width=250)
tree.column("Contato", anchor=CENTER, width=150)
tree.column("Pessoa", anchor=CENTER, width=70)
tree.column("RG", anchor=CENTER, width=130)
tree.column("Estado", anchor=CENTER, width=70)
tree.column("Endereço", anchor=CENTER, width=250)
tree.column("Cidade", anchor=CENTER, width=170)
tree.column("Bairro", anchor=CENTER, width=170)
tree.column("CEP", anchor=CENTER, width=130)
# Headings
tree.heading("#0", text="", anchor=CENTER)
tree.heading("ID", text="ID", anchor=CENTER)
tree.heading("Nome", text="Nome", anchor=CENTER)
tree.heading("CPF", text="CPF", anchor=CENTER)
tree.heading("Email", text="Email", anchor=CENTER)
tree.heading("Contato", text="Contato", anchor=CENTER)
tree.heading("Pessoa", text="Pessoa", anchor=CENTER)
tree.heading("RG", text="RG", anchor=CENTER)
tree.heading("Estado", text="Estado", anchor=CENTER)
tree.heading("Endereço", text="Endereço", anchor=CENTER)
tree.heading("Cidade", text="Cidade", anchor=CENTER)
tree.heading("Bairro", text="Bairro", anchor=CENTER)
tree.heading("CEP", text="CEP", anchor=CENTER)
# Row Tags
tree.tag_configure('oddrow', background="white")
tree.tag_configure('evenrow', background="lightblue")
# Add Record Entry Boxes and Dropdown Lists
data_frame = tk.LabelFrame(root, text="Dados do Cliente")
data_frame.pack(fill='x', expand=True, padx=20)
# Labels and Entries/Dropdowns Lists
name_label = tk.Label(data_frame, text="Nome")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(data_frame)
name_entry.grid(row=0, column=1, padx=10, pady=10)

rg_label = tk.Label(data_frame, text="RG")
rg_label.grid(row=0, column=2, padx=10, pady=10)
rg_entry = tk.Entry(data_frame)
rg_entry.grid(row=0, column=3, padx=10, pady=10)

cpf_label = tk.Label(data_frame, text="CPF")
cpf_label.grid(row=0, column=4, padx=10, pady=10)
cpf_entry = tk.Entry(data_frame)
cpf_entry.grid(row=0, column=5, padx=10, pady=10)

pessoa_label = tk.Label(data_frame, text="PF/PJ")
pessoa_label.grid(row=0, column=6, padx=10, pady=10)
pessoa_entry = tk.StringVar()
pessoa_entry.set("Física")  # Default value
pessoa_drop = tk.OptionMenu(data_frame, pessoa_entry, 'Física', 'Jurídica')
pessoa_drop.grid(row=0, column=7, padx=10, pady=10)

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

pessoa_label = tk.Label(data_frame, text="Estado")
pessoa_label.grid(row=1, column=6, padx=10, pady=10)
estado_entry = tk.StringVar()
estado_entry.set("CE")  # Default value
pessoa_drop = tk.OptionMenu(data_frame, estado_entry, *ESTADOS)
pessoa_drop.grid(row=1, column=7, padx=10, pady=10)

endereco_label = tk.Label(data_frame, text="Endereço")
endereco_label.grid(row=2, column=0, padx=10, pady=10)
endereco_entry = tk.Entry(data_frame)
endereco_entry.grid(row=2, column=1, padx=10, pady=10)

cidade_label = tk.Label(data_frame, text="Cidade")
cidade_label.grid(row=2, column=2, padx=10, pady=10)
cidade_entry = tk.Entry(data_frame)
cidade_entry.grid(row=2, column=3, padx=10, pady=10)

bairro_label = tk.Label(data_frame, text="Bairro")
bairro_label.grid(row=2, column=4, padx=10, pady=10)
bairro_entry = tk.Entry(data_frame)
bairro_entry.grid(row=2, column=5, padx=10, pady=10)

cep_label = tk.Label(data_frame, text="CEP")
cep_label.grid(row=2, column=6, padx=10, pady=10)
cep_entry = tk.Entry(data_frame)
cep_entry.grid(row=2, column=7, padx=10, pady=10, sticky=W)

# Buttons Functions


def add_record():
    _, nome, cpf, email, contato, pessoa, rg, estado, endereco, cidade, bairro, cep = get_entries()
    database.add_client(nome, cpf, email, contato, pessoa,
                        rg, estado, endereco, cidade, bairro, cep)
    # Clear entry boxes and Refresh the table
    refresh_table()


def remove_record():
    # Remove from database
    client_list = get_entries()
    id = client_list[0]
    database.delete_client(id)
    # Remove from the Treeview
    x = tree.selection()[0]
    tree.delete(x)


def update_record():
    # Update the database
    id, nome, cpf, email, contato, pessoa, rg, estado, endereco, cidade, bairro, cep = get_entries()
    database.update_client(id, nome, cpf, email, contato, pessoa,
                           rg, estado, endereco, cidade, bairro, cep)
    # Grab record number
    selected = tree.focus()
    # Update record in the Treeview
    tree.item(selected, text='',
              values=(id_entry.get(), name_entry.get(), cpf_entry.get(),
                      email_entry.get(), contato_entry.get(),
                      pessoa_entry.get(), rg_entry.get(), estado_entry.get(),
                      endereco_entry.get(), cidade_entry.get(),
                      bairro_entry.get(), cep_entry.get(),
                      )
              )
    clear_entries()


def select_record(e):
    # Clear entry boxes
    clear_entries()
    # Grab record Number
    selected = tree.focus()
    # Grab record values
    values = tree.item(selected, 'values')
    # Print outputs
    id_entry.insert(0, values[0])
    name_entry.insert(0, values[1])
    cpf_entry.insert(0, values[2])
    email_entry.insert(0, values[3])
    contato_entry.insert(0, values[4])
    pessoa_entry.set(values[5])
    rg_entry.insert(0, values[6])
    estado_entry.set(values[7])
    endereco_entry.insert(0, values[8])
    cidade_entry.insert(0, values[9])
    bairro_entry.insert(0, values[10])
    cep_entry.insert(0, values[11])


def query_database():
    records = database.query()
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            tree.insert(parent='', index='end', iid=count, text='',
                        values=(record[0], record[1], record[2],
                                record[3], record[4], record[5],
                                record[6], record[7], record[8],
                                record[9], record[10], record[11],
                                ),
                        tags=('evenrow', ))
        else:
            tree.insert(parent='', index='end', iid=count, text='',
                        values=(record[0], record[1], record[2],
                                record[3], record[4], record[5],
                                record[6], record[7], record[8],
                                record[9], record[10], record[11],
                                ),
                        tags=('oddrow', ))
        count += 1


def clear_entries():
    # Clear entry boxes
    name_entry.delete(0, END)
    rg_entry.delete(0, END)
    name_entry.delete(0, END)
    cpf_entry.delete(0, END)
    email_entry.delete(0, END)
    contato_entry.delete(0, END)
    id_entry.delete(0, END)
    endereco_entry.delete(0, END)
    cidade_entry.delete(0, END)
    bairro_entry.delete(0, END)
    cep_entry.delete(0, END)


def get_entries():
    id = id_entry.get()
    nome = name_entry.get()
    pessoa = pessoa_entry.get()
    cpf = cpf_entry.get()
    email = email_entry.get()
    contato = contato_entry.get()
    rg = rg_entry.get()
    estado = estado_entry.get()
    endereco = endereco_entry.get()
    cidade = cidade_entry.get()
    bairro = bairro_entry.get()
    cep = cep_entry.get()

    client_list = [id, nome, cpf, email, contato, pessoa,
                   rg, estado, endereco, cidade, bairro, cep]

    return client_list


def refresh_table():
    # Clear entries
    clear_entries()
    # Clear the Treeview Table
    tree.delete(*tree.get_children())  # row1, row2 ...
    # ReQueryTreeview table
    query_database()


def search_client():
    # Finding the best match
    tuple_list = database.query_name()  # [('',), ('',), ...]
    names_list = [name[0] for name in tuple_list]  # ['', '', ...]
    name = name_entry.get()
    match_list = difflib.get_close_matches(name, names_list, 3, 0.6)
    match = match_list[0]
    # Printing client's info
    records = database.query()
    for record in records:
        if record[1] == match:
            clear_entries()
            id_entry.insert(0, record[0])
            name_entry.insert(0, record[1])
            cpf_entry.insert(0, record[2])
            email_entry.insert(0, record[3])
            contato_entry.insert(0, record[4])
            pessoa_entry.set(record[5])
            rg_entry.insert(0, record[6])
            estado_entry.set(record[7])
            endereco_entry.insert(0, record[8])
            cidade_entry.insert(0, record[9])
            bairro_entry.insert(0, record[10])
            cep_entry.insert(0, record[11])


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

clear_button = tk.Button(
    button_frame, text="Limpar Campos", command=clear_entries)
clear_button.grid(row=0, column=3, padx=10, pady=10)

update_table_button = tk.Button(
    button_frame, text="Atualizar Tabela", command=refresh_table)
update_table_button.grid(row=0, column=4, padx=10, pady=10)

search_button = tk.Button(
    button_frame, text="Pesquisar Cliente pelo Nome", command=search_client)
search_button.grid(row=0, column=5, padx=10, pady=10)

# Bind Treeview
tree.bind("<ButtonRelease-1>", select_record)

# Run to pull data from database
query_database()

if __name__ == '__main__':
    root.mainloop()
