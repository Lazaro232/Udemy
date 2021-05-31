from collections import deque


friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    # Prepara o generator
    g.send(None)  # Roda a função até encontrar o yield
    while True:
        greeting = yield
        g.send(greeting)


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
greeter.send('Hello')
greeter.send('Hello')


'''
    Anotações

1) Generator que RECEBEM dados são chamados de CO-ROUTINE

2) .send(None) faz com que o co-routine rode até encontrar um yield.
Serve como uma preparação

3) Fluxo do código:
greeter.send(None) --> Faz greet(g) rodar até encontrar greeting = yield, o que faz 
com que g.send(None) (linha 16) rode friend_upper() até encontrar greeting = yield. 
Depois disso, volta para greet(b) e continua no loop while, que recebe o 'Hello', 
armazena ele no yield, que passa para a variável greeting, que é passada para
friend_upper() através do comando g.send(greeting). Dessa forma, o greeting
presente em friend_upper() recebe 'Hello' e printa: print(f'{greeting} {friend}')


'''
