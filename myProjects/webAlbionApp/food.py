from libs.open_market import OpenMarket
from utils.item_value import ItemValue
from utils.recipes import Recipes
from calc import Calculations


class Food:
    def __init__(self):
        self.meal = OpenMarket()
        self.calc = Calculations()

    def get_user_info(self):
        amount_to_craft = float(
            input('Quantidade a ser fabricada (e.g, 100): '))
        tax_fee = float(input('Taxa da loja a ser utilizada (e.g, 50): '))/100
        focus = int(input('1: Com foco --- 0: Sem foco '))
        return amount_to_craft, tax_fee, focus

    def omelette_t3(self):
        # Albion informations
        (omelette, wheat, chicken, hen) = self.meal.omelette_t3()
        # User informations
        (amount_to_craft, tax_fee, focus) = self.get_user_info()
        user_info = [amount_to_craft, tax_fee, focus]
        city_result = {}
        for city_info in range(len(omelette)):
            omelette_price = omelette[city_info]['price']
            wheat_price = wheat[city_info]['price']
            chicken_price = chicken[city_info]['price']
            hen_price = hen[city_info]['price']
            city = omelette[city_info]['city']

            omelette_info = [
                [omelette_price, ItemValue.OMELETTE["T3"]],
                [wheat_price, Recipes.OMELETTE['T3']['wheat']],
                [chicken_price, Recipes.OMELETTE['T3']['chicken']],
                [hen_price, Recipes.OMELETTE['T3']['hen']]
            ]

            # Calculations
            result = self.calc.calculations(user_info, omelette_info, city)
            result_dict = {city: result}
            city_result.update(result_dict)

        return city_result

    def omelette_t5(self):
        # Albion informations
        (omelette, cabbage, goose, goose_eggs) = self.meal.omelette_t5()
        # User informations
        (amount_to_craft, tax_fee, focus) = self.get_user_info()
        user_info = [amount_to_craft, tax_fee, focus]
        city_result = {}
        for city_info in range(len(omelette)):
            omelette_price = omelette[city_info]['price']
            cabbage_price = cabbage[city_info]['price']
            goose_price = goose[city_info]['price']
            goose_egs_price = goose_eggs[city_info]['price']
            city = omelette[city_info]['city']

            omelette_info = [
                [omelette_price, ItemValue.OMELETTE["T5"]],
                [cabbage_price, Recipes.OMELETTE['T5']['cabbage']],
                [goose_price, Recipes.OMELETTE['T5']['goose']],
                [goose_egs_price, Recipes.OMELETTE['T5']['goose_eggs']]
            ]

            # Calculations
            result = self.calc.calculations(user_info, omelette_info, city)
            result_dict = {city: result}
            city_result.update(result_dict)

        return city_result

    def omelette_t7(self):
        # Albion informations
        (omelette, corn, pork, goose_eggs) = self.meal.omelette_t7()
        # User informations
        (amount_to_craft, tax_fee, focus) = self.get_user_info()
        user_info = [amount_to_craft, tax_fee, focus]
        city_result = {}
        for city_info in range(len(omelette)):
            omelette_price = omelette[city_info]['price']
            corn_price = corn[city_info]['price']
            pork_price = pork[city_info]['price']
            goose_egs_price = goose_eggs[city_info]['price']
            city = omelette[city_info]['city']

            omelette_info = [
                [omelette_price, ItemValue.OMELETTE["T7"]],
                [corn_price, Recipes.OMELETTE['T7']['corn']],
                [pork_price, Recipes.OMELETTE['T7']['pork']],
                [goose_egs_price, Recipes.OMELETTE['T7']['goose_eggs']]
            ]

            # Calculations
            result = self.calc.calculations(user_info, omelette_info, city)
            result_dict = {city: result}
            city_result.update(result_dict)

        return city_result
