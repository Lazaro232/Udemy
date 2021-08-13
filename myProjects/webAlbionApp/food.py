from libs.open_market import OpenMarket
from utils.item_value import ItemValue
from utils.recipes import Recipes
from calc import Calculations


class Food:
    def __init__(self):
        self.meal = OpenMarket()
        self.calc = Calculations()

    def omelette(self, user_info: list, food_name: str):
        # Albion informations
        (omelette, ingredient_1, ingredient_2,
         ingredient_3) = self.meal.omelette(food_name)

        # User information
        if food_name == "omelette_t3":
            tier = "T3"
            ing_1_tag = "wheat"
            ing_2_tag = "chicken"
            ing_3_tag = "hen"

        elif food_name == "omelette_t5":
            tier = "T5"
            ing_1_tag = "cabbage"
            ing_2_tag = "goose"
            ing_3_tag = "goose_eggs"

        elif food_name == "omelette_t7":
            tier = "T7"
            ing_1_tag = "corn"
            ing_2_tag = "pork"
            ing_3_tag = "goose_eggs"

        city_result = {}
        for city_info in range(len(omelette)):
            omelette_price = omelette[city_info]['price']
            ing_1_price = ingredient_1[city_info]['price']
            ing_2_price = ingredient_2[city_info]['price']
            ing_3_price = ingredient_3[city_info]['price']
            city = omelette[city_info]['city']

            omelette_info = [
                [omelette_price, ItemValue.OMELETTE[tier]],
                [ing_1_price, Recipes.OMELETTE[tier][ing_1_tag]],
                [ing_2_price, Recipes.OMELETTE[tier][ing_2_tag]],
                [ing_3_price, Recipes.OMELETTE[tier][ing_3_tag]]
            ]

            # Calculations
            result = self.calc.calculations(user_info, omelette_info, city)
            result_dict = {city: result}
            city_result.update(result_dict)

        return city_result
