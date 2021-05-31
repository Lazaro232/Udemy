import time
import random

from threading import Thread

counter = 0  # Variável global


def increment_counter():
    global counter
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f'new counter value: {counter}')
    time.sleep(random.random())
    print('------------')


for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()


'''
    Anotações

1) Atomic Operations: são processos que NÃO PODEM ser interrompidos no meio.
Um exemplo disso é o print(), visto que não se pode printar metade de algo.

2) Deve-se ter cuidado ao usar Multi Thread quando se trata de varáveis
compartilhadas entre os Threads, pois eles podem acabar modificando ela
de forma desordenada (Como no exemplo acima)

3) Colocar tempos entre as linhas como feito acima é uma técnica chamda de 
FUZZYING

4) OBS.: NÃO USAR MULTI THREAD QUANDO SE DESEJA QUE ALGO SEJA SEQUENCIAL.
Caso precise, ver o próximo código (06_Queuing_Threads.py)

'''
