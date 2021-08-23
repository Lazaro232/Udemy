import tkinter as tk
from tkinter import ttk


def greet():  # Printa o que for digitado OU World se nada for digitado
    print(f"Hello, {user_name.get() or 'World'}")


# Instanciando o objeto Tkinter
root = tk.Tk()
root.title("Greeter")
# Variável que armazena o input do usuário
user_name = tk.StringVar()
# Label
name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
# Input (Entry)
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()
# Botao Greet
greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill='x', expand=True)

root.mainloop()


'''
Anotaçoes:

1) padx=(0, 10)
Adiciona 10 pixels a direita da Label criada acima.
Assim, outro objeto irá vir 10 pixels após a label

2) user_name = tk.StringVar()
.StringVar() é um objeto que rastreia as entradas do usuário
para o .Entry. Ou seja, transforma o que for digitado em uma string

3) .focus()
Faz com que o elemento apareça com um certo foco na janela

4) user_name.get()
Método get usado para recuperar o conteúdo da variável user_name
'''
