# Site: https://books.toscrape.com/
# Programa que baixa um página de livros e retorna o livro de menor valor

import requests

from pages.books_page import BookPage

page_content = requests.get('https://books.toscrape.com/').content
page = BookPage(page_content)
# print(page)

for book in page.books:
    print(book)

prices = [book.price for book in page.books]
titles = [book.title for book in page.books]
# Valor mínimo
min_value = min(prices)  # Retorna o menor valor dos livros
index_cheaper = prices.index(min_value)  # Posição do livro mais barato
cheaper_book = titles[index_cheaper]
# Valor Máximo
max_value = max(prices)
index_expensive = prices.index(max_value)
expensive_book = titles[index_expensive]

print(
    f'''\nThe cheaper book is: {cheaper_book} and it costs: £{min_value}
The most expensive one is: {expensive_book} and it costs £{max_value}''')
