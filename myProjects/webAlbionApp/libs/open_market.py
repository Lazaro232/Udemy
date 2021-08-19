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
        _, tier_string = food_name.split("_")  # ['omelette', 't3']
        tier = tier_string.upper()  # 'T3'
        if 'omelette' in food_name:
            item_value_dict = ItemValue.OMELETTE
            recipe_dict = Recipes.OMELETTE

        elif 'stew' in food_name:
            item_value_dict = ItemValue.STEW
            recipe_dict = Recipes.STEW

        elif 'sandwich' in food_name:
            item_value_dict = ItemValue.SANDWICH
            recipe_dict = Recipes.SANDWICH

        elif 'roast' in food_name:
            item_value_dict = ItemValue.ROAST
            recipe_dict = Recipes.ROAST

        elif 'pie' in food_name:
            item_value_dict = ItemValue.PIE
            recipe_dict = Recipes.PIE

        elif 'salad' in food_name:
            item_value_dict = ItemValue.SALAD
            recipe_dict = Recipes.SALAD

        elif 'soup' in food_name:
            item_value_dict = ItemValue.SOUP
            recipe_dict = Recipes.SOUP

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
