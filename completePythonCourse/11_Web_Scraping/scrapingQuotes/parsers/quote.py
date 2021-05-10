# Recebe uma TAG e retorna dados de uma QUOTE (citação do site) dentro da referida TAG
# https://quotes.toscrape.com/

from locators.quote_locators import QuoteLocators


# Dado uma QUOTE específica, encontra os dados acerta da QUOTE (CONTENT, AUTHOR, TAGS)
class QuoteParser:
    def __init__(self, parent):  # parent = div que possui class="quote"
        self.parent = parent

    def __repr__(self):  # Printa de forma mais bonita
        return f'<Quote {self.content}, by {self.author}'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        # Dentro de parent (div.quote), procura-se pelo locator
        return self.parent.select_one(locator).string
        # BeautifulSoup permite pesquisar dentro do próprio Locator, não
        # precisa ser um html completo.

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        # Retorna o texto de cada tag em uma lista
        return [e.string for e in self.parent.select_one(locator).string]
