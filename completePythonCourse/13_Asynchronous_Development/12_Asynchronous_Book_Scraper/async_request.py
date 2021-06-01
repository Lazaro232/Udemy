import aiohttp
import async_timeout
import asyncio
import time

'''
Code for testing purposes. Testing aiohhtp library
'''


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')
            # Retorna o código da resposta do servidor (200, por exemplo)
            return response.status


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

loop = asyncio.get_event_loop()
# Criando tarefas (50 requisições ao Google.com)
urls = ['http://google.com' for i in range(50)]
start = time.time()
# Roda até que get_multiple_pages() retorne algo, ou seja, tenha terminado
loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'All took {time.time() - start}')


'''
    Anotações

1) Ao se usar o assincronismo, é possível fazer uma tarefa (requisição neste caso)
esperar enquanto outra é executada. Dessa forma, por exemplo, é possível executar
inúmeras tarefas +- juntas. Ou seja, quando a tarefa 1 terminar de estabelecer 
conexão com o servidor, ela passa a esperar e a tarefa 2 passa a estebelecer
a referida conexão, só então a tarefa 1 passa para o próximo passo. Dessa forma, 
as tarefas finalizarão +- juntas.

2) aiohttp.ClientSession()

Cria uma "pool" de sessões
Além disso, ontém um armazém de COOKIES que compartilha os COOKIES enviados
pelos websites entre as requests realizadas.

OBS.: Em qualquer asycn with, o código pode ser parado e retomado, possiblitando
o desenvolvimento assíncrono do código.

3) asyncio.gather()

Basicamente espera todas as tarefas e só retorna quando TODAS estão completas

4) async with async_timeout.timeout(10):

Acusa erro após 10 segundos caso alguma tarefa demore demais

'''
