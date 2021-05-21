from utils import database

from utils.excel import ExcelCreator


def prompt_add_user():
    name = input('Nome: ').title()
    password = input('Senha: ')
    email = input('e-mail: ')
    logo = input('URL da Logo: ')
    database.add_user(name, password, email, logo)


def list_all_users():
    users = database.get_all_users()
    for user in users:
        print(
            f"ID: {user['id']}, Nome: {user['name']}, Senha: {user['password']}, e-mail: {user['email']}, Logo: {user['logo']}")


def prompt_update_user():
    id = input('ID do usuário que deseja modificar: ')
    name = input('Nome: ').title()
    password = input('Senha: ')
    email = input('e-mail: ')
    logo = input('URL da Logo: ')
    database.update_investment(id, name, password, email, logo)


def prompt_delete_user():
    id = input('ID da transação que deseja exlcuir: ')
    database.delete_investment(id)


# database.create_users_table()
# prompt_add_user()
# prompt_add_user()
# list_all_users()


excel = ExcelCreator()  # Instanciando objeto
excel.update_excel_file()  # Adicionando dados no excel
excel.inserting_image()  # Adicionando imagem no excel
excel.save_excel_file()  # Salvando arquivo Excel
