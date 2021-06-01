import logging
from bs4 import BeautifulSoup

from locators.all_books_page import AllBooksPageLocators
# re =  Regular Expression que já foi importado
from parsers.book_parser import BookParser, re

logger = logging.getLogger('scraping.all_books_page')


class AllBooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(
            f'Finding all books in the page using `{AllBooksPageLocators.BOOKS}`.')
        locator = AllBooksPageLocators.BOOKS
        return [BookParser(e) for e in self.soup.select(locator)]
        # .select (diferente de .select_one) seleciona TODAS as instancias que contiverem
        # o LOCATOR contido na variável BOOKS (que está em AllBooksPageLocators ...
        # ... dentro da pasta locators)

        # Depois de descobrir todos esse elementos, é instanciado um objeto para cada um deles

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available...')
        locator = AllBooksPageLocators.PAGER
        content = self.soup.select_one(locator).string  # Page 1 of 50
        logger.info(f'Found number of catalogue available: `{content}`.')
        expression = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(expression, content)
        max_page_number = matcher.group(1)  # .group(1) = 50
        logger.debug(
            f'Extracted number of pages as integer: `{max_page_number}`.')

        return int(max_page_number)
