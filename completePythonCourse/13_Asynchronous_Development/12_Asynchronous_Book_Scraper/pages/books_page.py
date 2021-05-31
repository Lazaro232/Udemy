# Recebe os dados de uma página e passa para book.py para retirar alguma informação dos livros

from bs4 import BeautifulSoup

from locators.all_books_page import BookPageLocators
from parsers.book import BookParser


class BookPage():
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BookPageLocators.BOOK  # 'article.product_pod'
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]
