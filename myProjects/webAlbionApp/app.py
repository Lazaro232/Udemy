from libs.open_market import OpenMarket
from utils.item_value import ItemValue
from utils.recipes import Foods
from utils.fees import Fees
from math import floor


# from cachetools import cached, TTLCache

# URL BASE --> https://www.albion-online-data.com/api/v2/stats/Prices ...

# Omelete .1 --> .../T7_MEAL_OMELETTE%401.json
# Omelete .2 --> .../T7_MEAL_OMELETTE%402.json

# Beef .1 --> .../T8_MEAL_STEW%401.json
# Beef .2 --> .../T8_MEAL_STEW%402.json
# Beef .3 --> .../T8_MEAL_STEW%403.json

# Exemplo: ENDPOINT = "https://www.albion-online-data.com/api/v2/stats/Prices/T7_MEAL_OMELETTE%402.json"

# Formula para taxa de uso: Custo/Item = Taxa * 5 * Valor do item (valor fixo)

meal = OpenMarket()


def omelette_t3():
    # Albion informations
    (omelette, wheat, chicken, hen) = meal.omelette_t3()
    omelette_price = omelette[1]['price']
    wheat_price = wheat[1]['price']
    chicken_price = chicken[1]['price']
    hen_price = hen[1]['price']

    # User information
    amount_to_craft = float(input('Quantidade a ser fabricada: '))
    tax_fee = float(input('Taxa da loja a ser utilizada: '))/100
    focus = int(input('1: Com foco --- 0: Sem foco '))

    # Calculations
    tax_to_craft = tax_fee * 5 * ItemValue.OMELETTE["T3"]

    if focus:
        return_rate = 0.453
    else:
        return_rate = 0.152

    real_return_rate = 1 + return_rate + \
        return_rate**2 + return_rate**3 + return_rate**4

    amount_crafted = floor(amount_to_craft * real_return_rate / 10)*10
    material_cost = amount_to_craft/10 * (wheat_price * Foods.OMELETTE['T3']['wheat'] +
                                          chicken_price * Foods.OMELETTE['T3']['chicken'] +
                                          hen_price * Foods.OMELETTE['T3']['hen'])
    craft_cost = amount_crafted * tax_to_craft / 10
    sell_cost = omelette_price * Fees.MARKET_FEE * amount_crafted
    total_cost = material_cost + craft_cost + sell_cost

    gross_profit = omelette_price * amount_crafted
    result = gross_profit - total_cost
    final_result = abs(floor(result))

    if result < 0:
        return "Prejuízo de {:,} pratas".format(final_result).replace(',', '.')
    else:
        return "Lucro de {:,} pratas".format(final_result).replace(',', '.')


print(omelette_t3())
