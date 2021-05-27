import time
from threading import Thread


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'aks_user, {time.time() - start}')


def complex_calculation():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - start}')


# Single Thread

start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')

# Multi Thread

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()
thread2.start()

# Manda o THREAD PRINCIPAL esperar pelos thread1 e thread2
thread1.join()
thread2.join()

print(f'Two thread total time: {time.time() - start}')


'''
    Anotações
    
1) As funções que fazem com sistema esperar por uma resposta do usuário são
chamadas de BLOCKING OPERATION. Por exemplo: input()

2) Ao se rodar ask_user(), o programa fica PARADO esperando que o usuário
responda. Isso é uma ação do tipo: SINGLE THREAD

3) Ao se utilizar o módulo Thread, passa-se a poder realizar operações
MULTI THREAD, ou seja: caso o programa esteja parado na função ask_user()
esperando pela reposta do usuário, ele passa a executar complex_calculation()
enquanto o usuário não responde. Isso agiliza o programa.

3.1) NÃO se deve usar Thread para algo que SEMPRE usa a CPU, por exemplo:
complex_calculation(). Usa-se Thread somente para as chamdas BLOCK OPERATIONS.
Ou seja, para funções que fazem com que o programa fique parado esperando algo,
por exemplo: ask_user()

'''
