import tkinter as tk
from tkinter import ttk


# Instanciando o objeto Tkinter
root = tk.Tk()
# Definindo um 'main frame'
main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

# Elementos DENTRO do Frame main
tk.Label(main, text="Label Top", bg="red").pack(
    side="top", fill="both", expand=True)
tk.Label(main, text="Label Top", bg="red").pack(
    side="top", fill="both", expand=True)

# Elementos FORA dp Frame main
tk.Label(root, text="Label left", bg="green").pack(
    side="left", fill="both", expand=True)

root.mainloop()

'''
Anotaçoes:

1) main = ttk.Frame(root)
Cria uma frame em root

Deve-se notar que as Label Top's NAO estao dentro de root, mas sim
dentro de main, o que faz com que o segundo elemento de root seja
na verdade Label Left e nao as Lebel Top's
'''
