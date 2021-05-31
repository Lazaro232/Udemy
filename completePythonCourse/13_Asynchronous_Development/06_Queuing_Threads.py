import queue

from threading import Thread

counter = 0  # Variável global
job_queue = queue.Queue()  # Coisas a serem printadas
counter_queue = queue.Queue()  # Montante a ser incrementado em counter


def increment_manager():
    global counter
    while True:
        # Espera até um item estar disponível e então TRAVA na fila (QUEUE)
        # Ou seja, não permite outro Thread usar até que esteja pronto
        increment = counter_queue.get()
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f'New counter value: {counter}', '--------'))
        # Destrava a fila (QUEUE)
        counter_queue.task_done()


# daemon=True --> Roda continuamente até achar um erro
Thread(target=increment_manager, daemon=True).start()


def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()


Thread(target=printer_manager, daemon=True).start()


def increment_counter():
    counter_queue.put(1)


worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join()

counter_queue.join()
job_queue.join()

'''
    Anotações

1) increment = counter_queue.get() --> Impede que mais de 1 Thread acesse
a variável increment ao mesmo tempo

1.1) increment só será acessada por outro Thread quando o .task_done() for
executado

OBS.: PARA USAR MULTI THREADS EM PROCESSOS QUE DEVEM SER SEQUENCIAIS, É
PRECISO USAR FILAS (QUEUES) !!!

'''
