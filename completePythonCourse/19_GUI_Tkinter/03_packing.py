import tkinter as tk


# Instanciando o objeto Tkinter
root = tk.Tk()

tk.Label(root, text="Label left", bg="green").pack(
    side="left", fill="both", expand=True)

tk.Label(root, text="Label Top", bg="red").pack(
    side="top", fill="both", expand=True)
tk.Label(root, text="Label Top", bg="red").pack(
    side="top", fill="both", expand=True)

root.mainloop()

'''
Anotaçoes:

1) side="..."
Funciona como uma âncora. Ou seja, é onde o elemento estará "grudado"
ao elemento anterior ou a janela.

.pack(side="left") --> Prende Label 1 a esquerda da janela
.pack(side="top") --> Prende Label 2 ao topo da janela

2) fill="..."
2.1 fill="y" --> O elemento preenche a janela no eixo VERTICAL enquanto
a janela é expandida

2.2 fill="x" --> O elemento preenche a janela no eixo HORIZONTAL enquanto
a janela é expandida

2.3 fill="both" --> O elemento expande pelo espaço DISPONÍVEL

3) expand=True
Exije da janela o MÁXIMO espaço, obrigando outros elementos sem o expand=True
a tomarem apenas o espaço MÍNIMO necessário para eles

Obs.: O primeiro a ser setado tem prioridade

OBS.: Se side="top" o elemento toma todo o espaço necessário horizontal, o
que faz com que o próximo elemento venha ABAIXO dele.
      Se side="left" o elemento toma todo o espaço necessário vertical, o
que faz com que o próximo elemento venha A DIREITA dele.

*** Ou seja, o que de fato define a posiçao de um elemento é
    qual SIDE o elemento anterior possui
'''
