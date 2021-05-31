def countdown(n):
    while n > 0:
        yield n
        n -= 1


tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished')

'''
    Anotações

1) Generators funcionam de forma PARECIDA com threads, pois com eles
conseguimos parar uma ação e retomá-la

2) Usar generators custa menos ao precessamento do código do que 
usar threads

'''
