import requests

from cachetools import cached, TTLCache
from utils.endpoints import EndPoints


class OpenMarket:
    BASE_URL = "https://www.albion-online-data.com/api/v2/stats/Prices"

    CITY_OPTIONS = ['Thetford', 'Fort Sterling',
                    'Lymhurst', 'Martlock', 'Caerleon', 'Bridgewatch']

    # Definir um método INIT que receba qual comida deve ser trabalhada

    @cached(cache=TTLCache(maxsize=3, ttl=900))
    def retrieve_data(self, url):
        # endpoint z= f"{self.BASE_URL}/T7_MEAL_OMELETTE%402.json"
        endpoint = f"{self.BASE_URL}/{url}.json"
        return requests.get(endpoint).json()  # json --> Dicionário

    def printPrices(self):
        # Recuperando dados da API
        city_dict = self.retrieve_data("T3_WHEAT")
        # Printando cidades selecionadas em CITY_OPTIONS
        for city_data in city_dict:
            city = city_data['city']
            price = city_data['sell_price_min']
            if city in self.CITY_OPTIONS:
                print(f"{city} is: {price: ,}".replace(',', '.'))

    def omelette_t3(self):
        # TIER 3 (Chicken Omelette)
        omellete_t3 = EndPoints.RESOURCES["omelette_t3"]
        sheaf_of_wheat = EndPoints.RESOURCES["sheaf_of_wheat"]
        raw_chicken = EndPoints.RESOURCES["raw_chicken"]
        hen_eggs = EndPoints.RESOURCES["hen_eggs"]

        # Retrieving the data
        omelette_t3_data = self.retrieve_data(omellete_t3)
        wheat_data = self.retrieve_data(sheaf_of_wheat)
        chicken_data = self.retrieve_data(raw_chicken)
        hen_data = self.retrieve_data(hen_eggs)

        # Organazing the data
        omellete_t3_prices = self.organize_data(omelette_t3_data)
        wheat_prices = self.organize_data(wheat_data)
        chicken_prices = self.organize_data(chicken_data)
        hen_prices = self.organize_data(hen_data)

        return omellete_t3_prices, wheat_prices, chicken_prices, hen_prices

    def organize_data(self, data):
        list = [{"city": city['city'], "price": city['sell_price_min']}
                for city in data if city['city'] in self.CITY_OPTIONS]
        sorted_list = sorted(list, key=lambda x: x['city'])
        return sorted_list

    '''
    ANOTAÇÃO: CACHE
        # maxsize=2 --> O CACHE irá guardar os argumentos da função e o que ela retorna.
        Como a função 'retrieve_data' não possui argumentos, um maxsize=2 é suficiente.
        Se ela possuísse argumentos, o maxsize teria de aumentar

        # ttl = 900 --> Após quanto tempo de aplicação rodando será realizada uma ...
        ... REQUEST ao servidor novamente para atualizar o valor no CACHE
        Neste caso, após 900 segundos (15 minutos) será realizada uma REQUEST nova ao servidor.
    '''
