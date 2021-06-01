from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def get_friend():
    yield from friends


def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'HELLO {friend}'
        except StopIteration:
            pass


friend_generator = get_friend()
g = greet(friend_generator)

print(next(g))
print(next(g))

'''
    Anotações

1)

'''
