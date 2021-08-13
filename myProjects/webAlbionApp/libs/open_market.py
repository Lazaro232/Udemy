import requests
from cachetools import cached, TTLCache
from utils.endpoints import EndPoints


class OpenMarket:
    BASE_URL = "https://www.albion-online-data.com/api/v2/stats/Prices"

    CITY_OPTIONS = ['Thetford', 'Fort Sterling',
                    'Lymhurst', 'Martlock', 'Caerleon', 'Bridgewatch']

    @cached(cache=TTLCache(maxsize=3, ttl=900))
    def retrieve_data(self, url):
        endpoint = f"{self.BASE_URL}/{url}.json"
        return requests.get(endpoint).json()  # json --> Dicionário

    def organize_data(self, data):
        list = [{"city": city['city'], "price": city['sell_price_min']}
                for city in data if city['city'] in self.CITY_OPTIONS]
        sorted_list = sorted(list, key=lambda x: x['city'])
        return sorted_list

    def omelette(self, food_name):
        if food_name == "omelette_t3":
            ing_endpoint_1 = "sheaf_of_wheat"  # ing =  ingredient
            ing_endpoint_2 = "raw_chicken"
            ing_endpoint_3 = "hen_eggs"

        elif food_name == "omelette_t5":
            ing_endpoint_1 = "cabbage"
            ing_endpoint_2 = "raw_goose"
            ing_endpoint_3 = "goose_eggs"

        elif food_name == "omelette_t7":
            ing_endpoint_1 = "bundle_of_corn"
            ing_endpoint_2 = "raw_pork"
            ing_endpoint_3 = "goose_eggs"

        # Omelette endpoints
        omelette_endpoint = food_name
        omelette = EndPoints.RESOURCES[omelette_endpoint]
        ing_1 = EndPoints.RESOURCES[ing_endpoint_1]
        ing_2 = EndPoints.RESOURCES[ing_endpoint_2]
        ing_3 = EndPoints.RESOURCES[ing_endpoint_3]
        # Retrieving the data
        omelette_data = self.retrieve_data(omelette)
        ing_1_data = self.retrieve_data(ing_1)
        ing_2_data = self.retrieve_data(ing_2)
        ing_3_data = self.retrieve_data(ing_3)
        # Organazing the data
        omelette_prices = self.organize_data(omelette_data)
        ing_1_prices = self.organize_data(ing_1_data)
        ing_2_prices = self.organize_data(ing_2_data)
        ing_3_prices = self.organize_data(ing_3_data)

        return omelette_prices, ing_1_prices, ing_2_prices, ing_3_prices


'''
ANOTAÇÃO:
1) maxsize=2
--> O CACHE irá guardar os argumentos da função e o que ela retorna.
Como a função 'retrieve_data' não possui argumentos, um maxsize=2 é suficiente.
Se ela possuísse argumentos, o maxsize teria de aumentar

2) ttl = 900 -
-> Após quanto tempo de aplicação rodando será realizada uma ...
... REQUEST ao servidor novamente para atualizar o valor no CACHE. Neste caso,
após 900 segundos (15 minutos) será realizada uma REQUEST nova ao servidor.

3) URL BASE --> https://www.albion-online-data.com/api/v2/stats/Prices ...

4)
    Omelete .1 --> .../T7_MEAL_OMELETTE%401.json
    Omelete .2 --> .../T7_MEAL_OMELETTE%402.json
    Beef .1 --> .../T8_MEAL_STEW%401.json
    Beef .2 --> .../T8_MEAL_STEW%402.json
    Beef .3 --> .../T8_MEAL_STEW%403.json
Exemplo: ENDPOINT = "https://www.albion-online-data.com/api/v2/stats/Prices/T7_MEAL_OMELETTE%402.json"
'''
