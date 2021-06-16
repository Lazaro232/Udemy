import functools

'''
    Decorator --> É uma função que recebe uma função (High order function)
    e retorna uma função.
'''

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(access_level):
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(panel):
            if user.get('access_level') == access_level:
                return func(panel)
            else:
                raise PermissionError('You do not have enough access rights.')
        return secure_func
    return my_decorator


@user_has_permission('admin')
def my_function(panel):
    return f'Password for {panel} panel is 1234'


print(my_function('guest'))


'''
    Anotações:


1) Cria-se uma função chamada user_has_permission() que recebe o nível de acesso.
Dentro dessa função, cria-se um DECORATOR chamado my_decorator() que verifica
o nível de acesso do usuário e executa a função my_function() através da
função secure_func().

3) Utilizando a estrutura do DECORATOR, pode-se fazer @user_has_permission('admin')

'''
