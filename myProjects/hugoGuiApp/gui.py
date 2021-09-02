import tkinter as tk
from database import Database
from tkinter import ttk
from tkinter.constants import CENTER, E, END, NO, RIGHT, W, Y

ESTADOS = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
    'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]


def incluir():
    nome = nome_var.get()
    pessoa = pessoa_var.get()
    cpf = cpf_var.get()
    rg = rg_var.get()
    estado = estado_var.get()
    endereco = endereco_var.get()
    bairro = bairro_var.get()
    cidade = cidade_var.get()
    cep = cep_var.get()
    email = email_var.get()
    contato = contato_var.get()
    print(nome, pessoa, cpf, rg, estado,
          endereco, bairro, cidade, cep, email, contato)


# Initial Setup
root = tk.Tk()
root.title('HOME MÓVEIS PLANEJADOS')
root.geometry('1000x500')
notebook = ttk.Notebook(root)
notebook.pack(padx=5, pady=5)
database = Database()

# Frames - Tabs
width = 1000
height = 500
novo_frame = tk.Frame(notebook, width=width, height=height)
consulta_frame = tk.Frame(notebook, width=width, height=height)
orcamento_frame = tk.Frame(notebook, width=width, height=height)
contrato_frame = tk.Frame(notebook, width=width, height=height)
# Frames Grid
novo_frame.grid()
consulta_frame.grid()
orcamento_frame.grid()
contrato_frame.grid()
# Add Tabs
notebook.add(novo_frame, text="Novo")
notebook.add(consulta_frame, text="Consulta")
notebook.add(orcamento_frame, text="Orçamento")
notebook.add(contrato_frame, text="Contrato")
# Objects
nome_var = tk.StringVar()
pessoa_var = tk.StringVar()
pessoa_var.set("Física")  # Default value = "CE"
cpf_var = tk.StringVar()
rg_var = tk.StringVar()
estado_var = tk.StringVar()
estado_var.set("CE")  # Default value = "CE"
endereco_var = tk.StringVar()
bairro_var = tk.StringVar()
cidade_var = tk.StringVar()
cep_var = tk.StringVar()
contato_var = tk.StringVar()
email_var = tk.StringVar()
# Secondary Frames
nome_frame = tk.Frame(novo_frame, width=50)
nome_frame.grid(row=0, column=1, columnspan=3)
endereco_frame = tk.Frame(novo_frame, width=50)
endereco_frame.grid(row=2, column=1, columnspan=3)
cidade_frame = tk.Frame(novo_frame, width=50)
cidade_frame.grid(row=3, column=1, columnspan=3)
email_frame = tk.Frame(novo_frame, width=50)
email_frame.grid(row=4, column=1, columnspan=3)

# Labels
padx_label = 10
pady_label = 20
nome_label = tk.Label(novo_frame, text="Nome :",
                      padx=padx_label, pady=pady_label,
                      font="Helvetica 11 bold")
pessoa_label = tk.Label(novo_frame, text="Pessoa :",
                        padx=padx_label, pady=pady_label,
                        font="Helvetica 11 bold")
cpf_label = tk.Label(novo_frame, text="CNPJ/CPF :",
                     padx=padx_label, pady=pady_label,
                     font="Helvetica 11 bold")
rg_label = tk.Label(novo_frame, text="RG :",
                    padx=padx_label, pady=pady_label,
                    font="Helvetica 11 bold")
estado_label = tk.Label(novo_frame, text="Estado :",
                        padx=padx_label, pady=pady_label,
                        font="Helvetica 11 bold")
endereco_label = tk.Label(novo_frame, text="Endereço :",
                          padx=padx_label, pady=pady_label,
                          font="Helvetica 11 bold")
bairro_label = tk.Label(novo_frame, text="Bairro :",
                        padx=padx_label, pady=pady_label,
                        font="Helvetica 11 bold")
cidade_label = tk.Label(novo_frame, text="Cidade :",
                        padx=padx_label, pady=pady_label,
                        font="Helvetica 11 bold")
cep_label = tk.Label(novo_frame, text="CEP :",
                     padx=padx_label, pady=pady_label,
                     font="Helvetica 11 bold")
email_label = tk.Label(novo_frame, text="Email :",
                       padx=padx_label, pady=pady_label,
                       font="Helvetica 11 bold")
contato_label = tk.Label(novo_frame, text="Contato :",
                         padx=padx_label, pady=pady_label,
                         font="Helvetica 11 bold")
# Label Grid
sticky_side_label = E
nome_label.grid(row=0, column=0, sticky=sticky_side_label)
pessoa_label.grid(row=0, column=4, sticky=sticky_side_label)
cpf_label.grid(row=1, column=0, sticky=sticky_side_label)
rg_label.grid(row=1, column=2, sticky=sticky_side_label)
estado_label.grid(row=1, column=4, sticky=sticky_side_label)
endereco_label.grid(row=2, column=0, sticky=sticky_side_label)
bairro_label.grid(row=2, column=4, sticky=sticky_side_label)
cidade_label.grid(row=3, column=0, sticky=sticky_side_label)
cep_label.grid(row=3, column=4, sticky=sticky_side_label)
email_label.grid(row=4, column=0, sticky=sticky_side_label)
contato_label.grid(row=4, column=4, sticky=sticky_side_label)

# Entries
width_entry = 3
nome_entry = tk.Entry(nome_frame, width=50, borderwidth=width_entry,
                      textvariable=nome_var)
cpf_entry = tk.Entry(novo_frame, borderwidth=width_entry,
                     textvariable=cpf_var)
rg_entry = tk.Entry(novo_frame, borderwidth=width_entry,
                    textvariable=rg_var)
endereco_entry = tk.Entry(endereco_frame, width=50, borderwidth=width_entry,
                          textvariable=endereco_var)
bairro_entry = tk.Entry(novo_frame, borderwidth=width_entry,
                        textvariable=bairro_var)
cidade_entry = tk.Entry(cidade_frame, width=50, borderwidth=width_entry,
                        textvariable=cidade_var)
cep_entry = tk.Entry(novo_frame, borderwidth=width_entry,
                     textvariable=cep_var)
email_entry = tk.Entry(email_frame, width=50, borderwidth=width_entry,
                       textvariable=email_var)
contato_entry = tk.Entry(novo_frame, borderwidth=width_entry,
                         textvariable=contato_var)
# Entry Grid
nome_entry.grid(row=0, column=1, sticky=W)
cpf_entry.grid(row=1, column=1, sticky=W)
rg_entry.grid(row=1, column=3, sticky=W)
endereco_entry.grid(row=2, column=3, sticky=W)
bairro_entry.grid(row=2, column=5, sticky=W)
cidade_entry.grid(row=3, column=3, sticky=W)
cep_entry.grid(row=3, column=5, sticky=W)
email_entry.grid(row=4, column=3, sticky=W)
contato_entry.grid(row=4, column=5, sticky=W)

# Dropdown List
estado_drop = tk.OptionMenu(novo_frame, estado_var, *ESTADOS)
estado_drop.grid(row=1, column=5, sticky=W)
cpfcnpj_drop = tk.OptionMenu(novo_frame, pessoa_var, 'Física', 'Jurídica')
cpfcnpj_drop.grid(row=0, column=5, sticky=W)

# Buttons + Empty Labels
empty_label = tk.Label(novo_frame).grid(row=5)
empty_label = tk.Label(novo_frame).grid(row=6)
empty_label = tk.Label(novo_frame).grid(row=7)
empty_label = tk.Label(novo_frame).grid(row=8)

incluir_button = tk.Button(
    novo_frame, text="Incluir", font="Arial 15 bold",
    width=7, bd=3, command=incluir)
incluir_button.grid(row=9, column=5)

# ----------------- CONSULTAS -----------------
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
tree_frame = tk.Frame(consulta_frame)
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
data_frame = tk.LabelFrame(consulta_frame, text="Dados do Cliente")
data_frame.pack(fill='x', expand=True, padx=20)

name_label = tk.Label(data_frame, text="Nome")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(data_frame)
name_entry.grid(row=0, column=1, padx=10, pady=10)

pessoa_label = tk.Label(data_frame, text="PF/PJ")
pessoa_label.grid(row=0, column=2, padx=10, pady=10)
pessoa_entry = tk.Entry(data_frame)
pessoa_entry.grid(row=0, column=3, padx=10, pady=10)

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
    pessoa_entry.delete(0, END)
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


# Buttons
button_frame = tk.LabelFrame(consulta_frame, text="Comandos")
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
