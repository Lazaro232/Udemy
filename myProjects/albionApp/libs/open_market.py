import requests

from cachetools import cached, TTLCache


class OpenMarket:
    BASE_URL = "https://www.albion-online-data.com/api/v2/stats/Prices"

    CITY_OPTIONS = ['Thetford', 'Fort Sterling',
                    'Lymhurst', 'Martlock', 'Caerleon', 'Bridgewatch']

    # Definir um método INIT que receba qual comida deve ser trabalhada

    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def meal(self):
        endpoint = f"{self.BASE_URL}/T7_MEAL_OMELETTE%402.json"
        return requests.get(endpoint).json()  # Dicionário

    def printPrices(self):
        city_dict = self.meal()
        for city_data in city_dict:
            city = city_data['city']
            price = city_data['sell_price_min']
            if city in self.CITY_OPTIONS:
                print(f"{city} is: {price: ,}".replace(',', '.'))
    '''
    ANOTAÇÃO: CACHE
        # maxsize=2 --> O CACHE irá guardar os argumentos da função e o que ela retorna.
        Como a função 'meal' não possui argumentos, um maxsize=2 é suficiente.
        Se ela possuísse argumentos, o maxsize teria de aumentar

        # ttl = 900 --> Após quanto tempo de aplicação rodando será realizada uma ...
        ... REQUEST ao servidor novamente para atualizar o valor no CACHE
        Neste caso, após 900 segundos (15 minutos) será realizada uma REQUEST nova ao servidor.
    '''
