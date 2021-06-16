import functools

'''
    Decorator --> É uma função que recebe uma função (High order function)
    e retorna uma função.
'''

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)
        else:
            raise PermissionError('You do not have enough access rights.')
    return secure_func


@user_has_permission
def my_function(panel):
    return f'Password for {panel} panel is 1234'


@user_has_permission
def another():
    return 'I\'m another'


print(my_function('guest'))
print(another())


'''
    Anotações:
1) Ao se possuir uma função que recebe parâmetros (my_function())
e outra que não recebe (another()), ocorrerá um erro, pois
caso NÃO se passe o parâmetro para secure_func(), my_function(panel)
não rodará; caso se passe o parâmetro, another() é quem não rodará.

2) Para corrigir isso, passa-se *args e **kwargs, pois significa que QUALQUER
quantidade de argumentos numéricos (*args) e nomeados (**kwargs) podem
ser passados.

3) O mesmo procedimento pode ser implementado para DECORATORS que possuam
argumentos, como visto na aula 04.

'''
