import time
from concurrent.futures import ThreadPoolExecutor


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

# Multi Thread Pool

start = time.time()

# Criando 2 Threads na "pool" de threads
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f'Two thread total time: {time.time() - start}')


'''
    Anotações
    
1) ThreadPoolExecutor cria uma "pool" de threads sem "target" e permite
usa essa "pool" para executar tarefas

2) Usando o 'with', não precisa usar o pool.shutdown()

'''
