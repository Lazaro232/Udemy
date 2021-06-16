import functools

'''
    Decorator --> É uma função que recebe uma função (High order function)
    e retorna uma função.
'''

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func


@user_has_permission
def my_function():
    return 'Password for admin panel is 1234'


print(my_function())

print(my_function.__name__)

'''
    Anotações:
1) @user_has_permission
"decora" a função my_function usando a função user_has_permission()

1.1) Porém, my_function() acaba ficando com o nome da função que de fato é
armazenada nela (secure_func() neste caso). Para que isso não ocorra,
é preciso informar ao python que secure_func() é apenas uma função que
acrescenta uma funcionalidade a outra função (user_has_permission()).

2) @functools.wraps(func)
informar ao python que secure_func() é apenas uma função que
acrescenta uma funcionalidade a outra função (user_has_permission()).

Desta forma, my_function() mantém seu nome e seus daos.

'''
