# Aceitando qualquer quantidade de argumentos --> *args

def add_all(*args):
    return sum(args)


print(add_all(1, 2, 3, 4))

# Aceitando qualquer quantidade de argumentos nomeados (named arguments) --> **kwargs


def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'For {k} we have {v}.')


pretty_print(username='jose123', access_level='admin')

# OU, pode-se passar o dicionário em si, fazendo o seguinte:

dictionaty = {'username': 'jose123', 'access_level': 'admin'}

# Precisa informar que são kwargs, para isso usa **
pretty_print(**dictionaty)

'''
    OBSERVAÇÃo
Ao invés de args e kwargs, pode usar qualquer nome, mas é PADRÃO do python
usar tais nomes.
'''
