from utils import database


def prompt_add_user():
    name = input('Nome: ').title()
    password = int(input('Senha: '))
    email = float(input('e-mail: '))
    logo = input('URL da Logo: ')
    database.add_user(name, password, email, logo)


def list_all_users():
    users = database.get_all_users()
    for user in users:
        print(
            f"ID: {user['id']}, Ativo: {user['name']}, N° Cotas: {user['password']}, Valor/Cota: {user['email']}, Data: {user['logo']}")


def prompt_update_user():
    id = input('ID do usuário que deseja modificar: ')
    name = input('Nome: ').title()
    password = int(input('Senha: '))
    email = float(input('e-mail: '))
    logo = input('URL da Logo: ')
    database.update_investment(id, name, password, email, logo)


def prompt_delete_user():
    id = input('ID da transação que deseja exlcuir: ')
    database.delete_investment(id)
