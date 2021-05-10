# Usado para exstrair informação de dentro de uma QUOTE (citação do site)
# https://quotes.toscrape.com/

class QuoteLocators:
    CONTENT = 'span.text'  # Locator que retorna: span que possui class="text"
    # Locator que retorna: small que possui class="author"
    AUTHOR = 'small.author'
    # Locator retorna: a que possui class="tag" que está dentro de div com class="tags"
    TAGS = 'div.tags a.tag'
