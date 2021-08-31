from utils import prompt


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
    "a": prompt.prompt_add_investment,       # Add
    "l": prompt.list_all_investments,        # List
    "o": prompt.organize_by_value_invested,  # Order
    "d": prompt.prompt_delete_investment,    # Delete
    "u": prompt.prompt_update_investment,    # Update
    "e": prompt.create_excel_file,           # Excel
}


def menu():
    prompt.database.create_investment_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in user_option:
            selected_function = user_option[user_input]
            selected_function()
        else:
            print('Unknown command. Please try again!')
        user_input = input(USER_CHOICE)


if __name__ == '__main__':
    menu()
