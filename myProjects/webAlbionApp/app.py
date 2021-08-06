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


def get_user_info():
    amount_to_craft = float(input('Quantidade a ser fabricada (e.g, 100): '))
    tax_fee = float(input('Taxa da loja a ser utilizada (e.g, 50): '))/100
    focus = int(input('1: Com foco --- 0: Sem foco '))
    return amount_to_craft, tax_fee, focus


def calculations(user_info: list, food_info: list, city: str):
    amount_to_craft = user_info[0]
    tax_fee = user_info[1]
    focus = user_info[2]
    food_price = food_info[0][0]
    item_value = food_info[0][1]

    tax_to_craft = tax_fee * 5 * item_value
    if focus:
        if city == 'Caerleon':
            return_rate = 0.479
        else:
            return_rate = 0.435
    else:
        if city == 'Caerleon':
            return_rate = 0.248
        else:
            return_rate = 0.152

    real_return_rate = 1 + return_rate + \
        return_rate**2 + return_rate**3 + return_rate**4

    amount_crafted = floor(amount_to_craft * real_return_rate / 10)*10

    resource_cost = 0
    for resource_info in food_info[1:]:
        resource_cost += resource_info[0] * resource_info[1]

    material_cost = amount_to_craft/10 * resource_cost
    craft_cost = amount_crafted * tax_to_craft / 10
    sell_cost = food_price * Fees.MARKET_FEE * amount_crafted
    total_cost = material_cost + craft_cost + sell_cost

    gross_profit = food_price * amount_crafted
    result = gross_profit - total_cost
    final_result = abs(floor(result))
    result_str = "de {:,} pratas".format(final_result).replace(',', '.')

    if result < 0:
        return f"{city}: Prejuízo {result_str}"
    else:
        return f"{city}: Lucro {result_str}"


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
        print(calculations(user_info, omelette_info, city))


omelette_t3()
