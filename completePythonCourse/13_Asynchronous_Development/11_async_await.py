from collections import deque
from types import coroutine


friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    await g

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
greeter.send('Hello')
greeter.send('Hello')


'''
    Anotações

1) await g faz o mesmo que: 
    g.send(None) 
    while True:
        greeting = yield
        g.send(greeting)

'''
