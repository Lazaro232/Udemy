import re  # Regular Expressions

from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''

# Ao se colocar os LOCATORS em uma classe diferente, facilita-se uma futura manutenção em caso
# de mudança desses LOCATORS.


class ParsedItemLocators:
    """
    Locators for an item in the HTML page.
    This allows us to easily see what our code will be looking at
    as well as change it quickly if we notice it is now different.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'

# OBS.: Cada LOCATOR segue uma hierarquia. Por exemplo: para chegar no NAME_LOCATOR é preciso
# entrar no article que possui a class=product_pod (article.product_pod) depois entrar no
# título h3 (h3) e por fim entrar no a (a)

# Outro exemplo. PRICE_LOCATOR: article com class=product_pod (article.product_pod) depois
# parágrafo com class=price_color (p.price_color)


class ParsedItem:
    """
    A class to take in an HTML page or content, and find properties of an item
    in it.
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocators.NAME_LOCATOR
        # .attrs['title'] é o mesmo que .attrs.get('title')
        item_name = self.soup.select_one(locator).attrs['title']
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocators.LINK_LOCATOR
        # .attrs['href'] é o mesmo que .attrs.get('href')
        item_url = self.soup.select_one(locator).attrs['href']
        return item_url

    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        # Retorna a string contida no Locator (£51.77)
        item_price = self.soup.select_one(locator).string
        # £ seguido de --> £
        # qualquer número entre 0 e 9, podendo ou não conter vírgula,  ...
        # ... com 1 ou mais (+) números --> [0-9,]+ seguido de um
        # . seguido de
        # qualquer número entre 0 e 9 com 1 ou mais (+) números --> [0-9]+
        pattern = '£([0-9,]+\.[0-9]+)'
        # Retorna uma string com o que bater entre o padrão (patter) e o 'alvo'
        matcher = re.search(pattern, item_price)
        # .group(1) retorna apenas o que estiver entre () e bater com o 'alvo'
        # .group(0) retorna TUDO que bater com o 'alvo'
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        star_rating_element = self.soup.select_one(locator)
        # .attrs['class'] é o mesmo que .attrs.get('class')
        classes = star_rating_element.attrs['class']
        # Poderia fazer assim: rating_classes = filter(lambda x: x != 'star-rating', classes)
        rating_classes = [x for x in classes if x != 'star-rating']
        return rating_classes[0]


item = ParsedItem(ITEM_HTML)
# NÃO precisa dos (), pois se usou o @property acima do método price
print(item.price)
print(item.rating)
