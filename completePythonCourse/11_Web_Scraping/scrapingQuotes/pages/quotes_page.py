# Retira dados da página de QUOTES (citação do site)
# https://quotes.toscrape.com/

from bs4 import BeautifulSoup

from locators.quote_pages_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotePage:
    def __init__(self, page):  # Recebe o conteúdo de uma página inteira
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        # QuotesPageLocators.QUOTE = 'div.quote'
        locator = QuotesPageLocators.QUOTE
        # Seleciona TODAS as divs que contiverem class="quote"
        quotes_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quotes_tags]
