'''
    Decorator --> É uma função que recebe uma função (High order function)
    e retorna uma função.
'''

user = {'username': 'jose123', 'access_level': 'admin'}

# Função que recebe outra função e retorna uma função = DECORATOR


def user_has_permission(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func


def my_function():
    return 'Password for admin panel is 1234'


my_secure_function = user_has_permission(my_function)

print(my_secure_function())
