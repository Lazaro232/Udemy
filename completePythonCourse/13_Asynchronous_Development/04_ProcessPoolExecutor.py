import time
from concurrent.futures import ProcessPoolExecutor


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


# Single Process

start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')

# Multi Processes Pool

start = time.time()

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)

print(f'Two process total time: {time.time() - start}')


'''
    Anotações
    
1) Quando usar MULTI PROCESS: Quando se deseja executar tarefas ao mesmo tempo,
por exemplo, executar complex_calculation() duas vezes ao mesmo tempo.

1.1) Quando se tem uma tarefa que faz com que o programa ESPERE, usa-se
MULTI THREAD e não MULTI PROCESS

'''
