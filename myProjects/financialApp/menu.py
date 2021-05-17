from utils import app

'''
Arquivo que contém o menu interativo com o usuário
'''

USER_CHOICE = """
Enter:
- 'a' to add a new investment
- 'l' to list all investments
- 'o' to order the investments by value invested
- 'd' to delete an investment
- 'u' to update an investiment
- 'e' to create an excel file
- 'q' to quit

Your choice: """

user_option = {
    "a": app.prompt_add_investment,       # Add
    "l": app.list_all_investments,        # List
    "o": app.organize_by_value_invested,  # Order
    "d": app.prompt_delete_investment,    # Delete
    "e": app.create_excel_file,         # Excel
}


def menu():
    app.database.create_investment_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in user_option:
            selected_function = user_option[user_input]
            selected_function()
        else:
            print('Unknown command. Please try again!')
        user_input = input(USER_CHOICE)


# FALTA ADICIONAR O UPDATE (MODIFICAR UM INVESTIMENTO JÁ ADICIONADO !!!!!!)
menu()
# FALTA ADICIONAR O UPDATE (MODIFICAR UM INVESTIMENTO JÁ ADICIONADO !!!!!!)
