# Usado para exstrair informação de dentro de uma PÁGINA, ou seja, vai retornar várias QUOTES
# e vai passar de 1 por 1 para quote_locators.py
# https://quotes.toscrape.com/

class QuotesPageLocators:
    # Locator que retorna: div (html) que possui a class="quote"
    QUOTE = 'div.quote'
