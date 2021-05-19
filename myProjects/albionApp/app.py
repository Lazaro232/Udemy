from libs.open_market import OpenMarket


# from cachetools import cached, TTLCache

# URL BASE --> https://www.albion-online-data.com/api/v2/stats/Prices ...

# Omelete .1 --> .../T7_MEAL_OMELETTE%401.json
# Omelete .2 --> .../T7_MEAL_OMELETTE%402.json

# Beef .1 --> .../T8_MEAL_STEW%401.json
# Beef .2 --> .../T8_MEAL_STEW%402.json
# Beef .3 --> .../T8_MEAL_STEW%403.json

# Exemplo: ENDPOINT = "https://www.albion-online-data.com/api/v2/stats/Prices/T7_MEAL_OMELETTE%402.json"


meal = OpenMarket()


MARKET_FEE = 0.045
RETURN_RATE = 0.152

# Formula para taxa de uso: Custo/Item = Taxa * 5 * Valor do item (valor fixo)

# Valor do omelete 7.0 = 504
# Valor do ometele 7.1/7.2/7.3 = 1080
item_value_70 = 504
item_value_7123 = 1080


def profit(how_much):
    (omelete, wheat, chicken, hen) = meal.omelette_t3()
