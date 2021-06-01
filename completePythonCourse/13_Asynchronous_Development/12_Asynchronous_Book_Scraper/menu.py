import logging

from app import books


logger = logging.getLogger('scraping.manu')

USER_CHOICE = ''' Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

Enter your choice: '''


def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    # sorted --> Organiza a lista de acordo com a KEY (no caso de acordo com as estrelas)
    # Multiplicar por -1 faz com que seja organizado de forma DESCENDENTE, ou seja, ...
    # De 5 estrelas para 1 e não de 1 para 5.
    # [:10] Pega apenas 10 livros (slice) --> 0 até o 9
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding best books by price...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)

# Caso se queira organizar de acordo com múltiplas características. Por exemplo, Organizar primeiro
# de acordo com as estrelas e dentre os que possuem o mesmo número de estrelas, organizar
# de acordo com o preço. Para isso, usa-se uma TUPLA, em que o primeiro elemento é o que será
# primeiro organizado (estrelas no caso abaixo) e o segundo será o segundo elemento a ser
# organizado (preço no caso abaixo)


def print_best_cheapest_books():
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))
    for book in best_books:
        print(book)


# Tupla usada para a função GENERATOR get_next_book()
books_generator = (x for x in books)


def get_next_book():
    logger.info('Getting next book from generator of all books...')
    print(next(books_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOICE)
    logger.debug('Terminatng program...')


menu()
