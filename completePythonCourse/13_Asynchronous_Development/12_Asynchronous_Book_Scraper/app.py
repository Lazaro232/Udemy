import aiohttp
import async_timeout
import asyncio
import time
import logging
import requests

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

loop = asyncio.get_event_loop()

books = page.books


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')
            # Retorna o conteúdo HTML da página
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    # Cria uma pool de sessões
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        # Roda todas as tarefas de uma vez usando o asyncio.gather
        # Sem o asyncio.gather, teria de fazer um .run_until_complete para cada tarefa
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

urls = ['https://books.toscrape.com/catalogue/page-{page_num+1}.html'
        for page_num in range(1, page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'Total page requests took {time.time() - start}')

for page_content in pages:
    logger.debug('Creating AllBookspgae from page content.')
    page = AllBooksPage(page_content)
    books.extend(page.books)  # extend = append para vários elementos
