import requests
from cachetools import cached, TTLCache
from utils.endpoints import EndPoints
from utils.item_value import ItemValue
from utils.recipes import Recipes


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

    def all_foods(self, food_name):
        # Food endpoints
        ing_list, item_value_dict, recipe_dict, tier = self.food_endpoint(
            food_name)
        food_endpoint = food_name
        food = EndPoints.RESOURCES[food_endpoint]
        ing_endpoint_list = []
        for ing in ing_list:
            ing_endpoint_list.append(EndPoints.RESOURCES[ing])

        # Retrieving the data
        food_data = self.retrieve_data(food)
        ing_data_list = []
        for ing in ing_endpoint_list:
            ing_data_list.append(self.retrieve_data(ing))

        # Organazing the data
        food_prices = self.organize_data(food_data)
        ing_price_list = []
        for ing in ing_data_list:
            ing_price_list.append(self.organize_data(ing))

        return food_prices, ing_price_list, ing_list, item_value_dict, recipe_dict, tier

    def food_endpoint(self, food_name):
        if 'omelette' in food_name:
            item_value_dict = ItemValue.OMELETTE
            recipe_dict = Recipes.OMELETTE
            if food_name == "omelette_t3":
                tier = "T3"
                tag_list = list(recipe_dict[tier].keys())

            elif food_name == "omelette_t5":
                tier = "T5"
                tag_list = list(recipe_dict[tier].keys())

            elif food_name == "omelette_t7":
                tier = "T7"
                tag_list = list(recipe_dict[tier].keys())

        elif 'stew' in food_name:
            item_value_dict = ItemValue.STEW
            recipe_dict = Recipes.STEW
            if food_name == "stew_t4":
                tier = "T4"
                tag_list = list(recipe_dict[tier].keys())

            elif food_name == "stew_t6":
                tier = "T6"
                tag_list = list(recipe_dict[tier].keys())

            elif food_name == "stew_t8":
                tier = "T8"
                tag_list = list(recipe_dict[tier].keys())

        elif 'sandwich' in food_name:
            item_value_dict = ItemValue.SANDWICH
            recipe_dict = Recipes.SANDWICH
            if food_name == "sandwich_t4":
                tier = "T4"
                tag_list = list(recipe_dict[tier].keys())

            elif food_name == "sandwich_t6":
                tier = "T6"
                tag_list = list(recipe_dict[tier].keys())

            elif food_name == "sandwich_t8":
                tier = "T8"
                tag_list = list(recipe_dict[tier].keys())

        return tag_list, item_value_dict, recipe_dict, tier


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
