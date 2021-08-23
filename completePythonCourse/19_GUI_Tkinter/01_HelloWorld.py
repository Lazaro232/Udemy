import tkinter as tk
from tkinter import ttk


def greet():
    print('Hello World')


# Instanciando o objeto Tkinter
root = tk.Tk()
root.title("Hello")

# Cria o botao
greet_button = ttk.Button(root, text="Greet", command=greet)
# Coloca o botao dentro de root
greet_button.pack(side="left", fill='x', expand=True)
# Criando botao para fechar a janela
quit_button = ttk.Button(root, text='Quit', command=root.destroy)
quit_button.pack(side='left', fill='x', expand=True)

root.mainloop()

'''
Anotaçoes:

1) root.mainloop()
Fica nessa linha até a janela ser fechada
'''
