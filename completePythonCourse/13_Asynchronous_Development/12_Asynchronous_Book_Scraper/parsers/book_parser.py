import re  # Regular Expressions
import logging

from locators.books_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    # Criando uma variável estática --> Como não está dentro de __init__, não pode ser modificada
    # Essa variável do tipo DICIONÁRIO irá converter a String advinda de rating () em um número
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        #logging.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, £{self.price} ({self.rating} stars)>' if self.rating > 1 else f'<Book {self.name}, £{self.price} ({self.rating} star)>'
    # star se self.rating = 1 e starS se self.rating > 1

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        # .attrs['title'] é o mesmo que .attrs.get('title')
        item_name = self.parent.select_one(locator).attrs['title']
        logger.debug(f'Found book name, `{item_name}`.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookLocators.LINK_LOCATOR
        # .attrs['href'] é o mesmo que .attrs.get('href')
        item_url = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link, `{item_url}`.')
        return item_url

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        # Retorna a string contida no Locator
        item_price = self.parent.select_one(locator).string
        # £ seguido de
        # qualquer número entre 0 e 9, podendo ou não conter vírgula,  ...
        # ... com 1 ou mais (+) números --> [0-9,]+ seguido de um
        # . seguido de
        # qualquer número entre 0 e 9 com 1 ou mais (+) números --> [0-9]+
        pattern = '£([0-9,]+\.[0-9]+)'
        # Retorna uma string com o que bater entre o padrão (pattern) e o 'alvo'
        matcher = re.search(pattern, item_price)
        # .group(1) retorna apenas o que estiver entre () e bater com o 'alvo'
        # .group(0) retorna TUDO que bater com o 'alvo'
        float_price = float(matcher.group(1))
        logger.debug(f'Found book price, `{float_price}`.')
        return float_price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_element = self.parent.select_one(locator)
        # .attrs['class'] é o mesmo que .attrs.get('class')
        classes = star_rating_element.attrs['class']
        # Poderia fazer assim: rating_classes = filter(lambda x: x != 'star-rating', classes)
        rating_classes = [x for x in classes if x != 'star-rating']
        # O método GET() usado em um dicionário (RATINGS) irá retornar o valor associado
        # a KEY passada para ele (rating_classes[0]). Por exemplo, se rating_classes[0] é
        # igual a 'Three', o getLogger()() retornará: 3
        # Retornará None se não for encontrada uma KEY em RATINGS que ...
        # ... corresposnda ao rating_classes[0]
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.debug(f'Found book rating, `{rating_number}`.')
        return rating_number
