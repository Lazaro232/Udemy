import tkinter as tk

from tkinter import ttk
from tkinter.constants import E, W

ESTADOS = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
    'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']


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
root.geometry('800x500')
notebook = ttk.Notebook(root)
notebook.pack(padx=5, pady=5)
# Frames - Tabs
width = 800
height = 700
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


if __name__ == '__main__':
    root.mainloop()
