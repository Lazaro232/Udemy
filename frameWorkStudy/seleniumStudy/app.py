# Usada para criar o DRIVER que contém o conteúdo da página
from selenium import webdriver
# Permite o uso do Enter, Backspace, Digitar em algum local, etc
from selenium.webdriver.common.keys import Keys
# Usadas para WAITS (espera até que certa condição tenha sido atendida)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://techwithtim.net")
print(driver.title)  # Printa o título da página

# Retorna o elemento na página que possua name= "s"
# Neste caso é uma barra de pesquisa
search = driver.find_element_by_name("s")

# Pesquisando algo na barra de pesquisa
search.send_keys("test")  # Digita "test" na barra de pesquisa
search.send_keys(Keys.RETURN)  # "aperta" Enter (RETURN)

# Acessando PAGE SOURCE (Inspect) da página
'''
print(driver.page_source)
'''

# Esperando a página ser carregada após realizar a pesquisa

# Espera no máximo até 10 segundos que haja um elemento com id="main" na página
# Porém, irá rodar antes dos 10s se o elemento aparecer antes. Se ele demorar além dos 10s ...
# ... ocorrerá um erro.
try:
    main = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "main"))
    )
    # Retorna todos OS "articles"
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        # Retorna O elementO que possui class="entry-summary"
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)

finally:
    driver.quit()  # Fecha o Browser inteiro // driver.close() --> Fecha apenas a ABA


# Acessando um elemento específico da página

# Procura pelo elemento com id="main"
'''
main = driver.find_element_by_id("main")
print(main.text)  # Printa o conteúdo dele (Igual ao .string do BeautifulSoup)
'''
