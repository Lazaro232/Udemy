# Usada para criar o DRIVER que contém o conteúdo da página
from selenium import webdriver
# Permite o uso do Enter, Backspace, Digitar em algum local, etc
from selenium.webdriver.common.keys import Keys
# Usadas para WAITS (espera até que certa condição tenha sido atendida)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

'''
ESSE ARQUIVO DEVE SER EXECUTADO NO WINDOWS !!!
MODIFICAR A PASTA DO chromedriver.exe !!!
'''

# PATH = "C:/wsl/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.albiononline2d.com/en/item/id/T7_MEAL_OMELETTE@1")

# Find the table with market prices

# Espera no máximo até 10 segundos que haja um elemento com id="market-table-body" na página
# Porém, irá rodar antes dos 10s se o elemento aparecer antes. Se ele demorar além dos 10s ...
# ... ocorrerá um erro.
try:
    price_table = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.ID, "market-table-body"))
    )
    # Retorna todos OS "tr" (linhas) dentro de price_table
    rows = price_table.find_elements_by_tag_name("tr")
    city_and_prices = []  # Lista vazia que irá armazenar as listas com cidade e preços
    for row in rows:
        cols = row.find_elements_by_tag_name('td')
        cols = [x.text.strip(':') for x in cols]
        city_and_prices.append(cols)

    # Organizando os dados
    city_and_prices_att = [[str(cp[0]), float(cp[1])]
                           for cp in city_and_prices]

    print(city_and_prices_att)

    bm = city_and_prices[0]
    bm_city = str(bm[0])
    # bm_city = str(bm[0]).strip(':')  # .strip(':') retira os : no final da string
    bm_price = float(bm[1])  # transforma a string em um float
    #print(f'{bm_city} has the price of: {bm_price}')


finally:
    driver.quit()  # Fecha o Browser inteiro // driver.close() --> Fecha apenas a ABA
