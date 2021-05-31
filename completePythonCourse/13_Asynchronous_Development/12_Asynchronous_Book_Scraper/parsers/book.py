# Dado o locator de um livro (parent) retornará o conteúdo desejado utilizando os
# locators contidos em books_locators.py

import re  # Regular Expressions

from locators.books_locators import BookLocators


class BookParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'The book {self.title} costs £{self.price}'

    @property
    def price(self):
        locator = BookLocators.PRICE  # 'div.product_price p.price_color'
        # Dentro de 'article.product_pod' (parent), procura-se por ...
        # ... 'div.product_price p.price_color' (locator) e retira-se ...
        # ... o seu conteúdo em forma de string (.string)
        book_price = self.parent.select_one(locator).string
        expression = '£([0-9,]+\.[0-9]+)'
        matcher = re.search(expression, book_price)
        price = float(matcher.group(1))

        return price

    @property
    def title(self):
        locator = BookLocators.TILTE
        title = self.parent.select_one(locator).attrs.get('title')
        return title
