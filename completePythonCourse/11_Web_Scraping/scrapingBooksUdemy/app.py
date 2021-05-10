import requests
import logging

from pages.all_books_page import AllBooksPage

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [ %(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')
# Tempo - Level(8 caracteres) - Nome do arquivo -  Nmr da linha -  Mensagem
# Formato da data: Dia-Mes-Ano Hora:Minutos:Segundos
# level=logging.DEBUG --> Mostra as mensagens de debug (se deu certo ou não)
# Pode-se usar level=logging.INFO, dessa forma aparece apenas o que eu colocar
# Como no exemplo abaixo: logger.info('Loading books list...')
# log.txt armazenará os LOGS
logger = logging.getLogger('scraping')

logger.info('Loading books list...')


# https://books.toscrape.com/catalogue/page-1.html


page_content = requests.get(
    'https://books.toscrape.com/catalogue/page-1.html').content
page = AllBooksPage(page_content)

books = page.books

for page_num in range(1, page.page_count):  # 1 até 49 (são 50 páginas)
    # Página 2 até 50, pois a 1 já está baixada acima
    url = f'https://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    logger.debug('Creating AllBookspgae from page content.')
    page = AllBooksPage(page_content)
    books.extend(page.books)  # extend = append para vários elementos
