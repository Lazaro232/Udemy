from typing import final
from libs.open_market import OpenMarket
from math import floor


# from cachetools import cached, TTLCache

# URL BASE --> https://www.albion-online-data.com/api/v2/stats/Prices ...

# Omelete .1 --> .../T7_MEAL_OMELETTE%401.json
# Omelete .2 --> .../T7_MEAL_OMELETTE%402.json

# Beef .1 --> .../T8_MEAL_STEW%401.json
# Beef .2 --> .../T8_MEAL_STEW%402.json
# Beef .3 --> .../T8_MEAL_STEW%403.json

# Exemplo: ENDPOINT = "https://www.albion-online-data.com/api/v2/stats/Prices/T7_MEAL_OMELETTE%402.json"


meal = OpenMarket()

FOODS = [{'food': 'omelette_T3',
          'wheat': 4,
          'chicken': 8,
          'hen': 2},
         {'food': 'omelette_T5',
          'cabbage': 12,
          'goose': 24,
          'goose_eggs': 6},
         {'food': 'omelette_T7',
          'corn': 36,
          'pork': 72,
          'goose_eggs': 18},
         ]


MARKET_FEE = 0.045

# Formula para taxa de uso: Custo/Item = Taxa * 5 * Valor do item (valor fixo)

# Valor do omelete 3.0 = 56,2
# Valor do omelete 5.0 = 168,1
# Valor do omelete 7.0 = 504
# Valor do ometele 7.1/7.2/7.3 = 1080
item_value_30 = 56.2
item_value_50 = 168.1
item_value_70 = 504
item_value_7123 = 1080


def profit():
    # Albion informations
    (omelette, wheat, chicken, hen) = meal.omelette_t3()
    omelette_price = omelette[1]['price']
    wheat_price = wheat[1]['price']
    chicken_price = chicken[1]['price']
    hen_price = hen[1]['price']

    # User information
    amount_to_craft = float(input('Quantidade a ser fabricada: '))
    tax_fee = float(input('Taxa da loja a ser utilizada: '))/100
    focus = int(input('1: With focus --- 0: Without focus '))

    # Calculator
    tax_to_craft = tax_fee * 5 * item_value_30

    if focus:
        return_rate = 0.453
    else:
        return_rate = 0.152

    real_return_rate = 1 + return_rate + \
        return_rate**2 + return_rate**3 + return_rate ** 4

    amount_crafted = floor(amount_to_craft * real_return_rate / 10)*10
    material_cost = amount_to_craft/10 * (wheat_price * FOODS[0]['wheat'] +
                                          chicken_price * FOODS[0]['chicken'] +
                                          hen_price * FOODS[0]['hen'])
    craft_cost = amount_crafted * tax_to_craft / 10
    sell_cost = omelette_price * MARKET_FEE * amount_crafted
    total_cost = material_cost + craft_cost + sell_cost

    gross_profit = omelette_price * amount_crafted
    result = gross_profit - total_cost
    final_result = abs(floor(result))

    if result < 0:
        return "Prejuízo de {:,} pratas".format(final_result).replace(',', '.')
    else:
        return "Lucro de {:,} pratas".format(final_result).replace(',', '.')


# profit()
print(profit())
