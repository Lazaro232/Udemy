from libs.open_market import OpenMarket
from utils.item_value import ItemValue
from utils.recipes import Foods
from calc import Calculations


meal = OpenMarket()
calc = Calculations()


def get_user_info():
    amount_to_craft = float(input('Quantidade a ser fabricada (e.g, 100): '))
    tax_fee = float(input('Taxa da loja a ser utilizada (e.g, 50): '))/100
    focus = int(input('1: Com foco --- 0: Sem foco '))
    return amount_to_craft, tax_fee, focus


def omelette_t3():
    # Albion informations
    (omelette, wheat, chicken, hen) = meal.omelette_t3()
    # User informations
    (amount_to_craft, tax_fee, focus) = get_user_info()
    user_info = [amount_to_craft, tax_fee, focus]

    for city_info in range(len(omelette)):
        omelette_price = omelette[city_info]['price']
        wheat_price = wheat[city_info]['price']
        chicken_price = chicken[city_info]['price']
        hen_price = hen[city_info]['price']
        city = omelette[city_info]['city']

        omelette_info = [
            [omelette_price, ItemValue.OMELETTE["T3"]],
            [wheat_price, Foods.OMELETTE['T3']['wheat']],
            [chicken_price, Foods.OMELETTE['T3']['chicken']],
            [hen_price, Foods.OMELETTE['T3']['hen']]
        ]

        # Calculations
        calc.calculations(user_info, omelette_info, city)


omelette_t3()
