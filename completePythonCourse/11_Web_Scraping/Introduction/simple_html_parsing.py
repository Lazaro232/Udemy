from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():  # Função que encontra o título (h1)
    print(simple_soup.find('h1').string)


def find_list_items():  # Função que encontra os itens de uma lista (li)
    list_items = simple_soup.find_all('li')
    list_content = [e.string for e in list_items]
    print(list_content)


def find_paragraph():  # Funçãoo que encontra o parágrafo (p) com o argumento class=subtitle
    print(simple_soup.find('p', {'class': 'subtitle'}).string)


def find_other_paragraph():  # Função que encontra parágrafos que NÃO contenha class=subtitle
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [
        p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0].string)

# OBS.: A função get() retorna um NONE quando não encontra nada. Porém um NONE não é iterável
# ... causando erro no FOR
# Para que o get() retorne algo que seja iterável, faz-se get(agr1, obj_iterável).
# No caso acima, usa-se uma lista vazia


find_title()
find_list_items()
find_paragraph()
find_other_paragraph()
