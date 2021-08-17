from libs.open_market import OpenMarket
from calc import Calculations


class Food:
    def __init__(self):
        self.meal = OpenMarket()
        self.calc = Calculations()

    def all_foods(self, user_info: list, food_name: str):
        # Albion informations
        food, ing_list, ing_tag_list, item_value_dict, recipe_dict, tier = self.meal.all_foods(
            food_name)

        city_result = {}
        for city_info in range(len(food)):
            food_price = food[city_info]['price']
            ing_price_list = []
            for ing in ing_list:
                ing_price = ing[city_info]['price']
                ing_price_list.append(ing_price)
            city = food[city_info]['city']

            food_info = [
                [food_price, item_value_dict[tier]]]
            for i in range(len(ing_price_list)):
                list_to_append = [ing_price_list[i],
                                  recipe_dict[tier][ing_tag_list[i]]]
                food_info.append(list_to_append)

            # Calculations
            result = self.calc.calculations(user_info, food_info, city)
            result_dict = {city: result}
            city_result.update(result_dict)

        return city_result
