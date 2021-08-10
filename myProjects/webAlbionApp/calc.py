from utils.fees import Fees
from math import floor

# Formula para taxa de uso: Custo/Item = Taxa * 5 * Valor do item (valor fixo)


class Calculations:
    def calculations(self, user_info: list, food_info: list, city: str):
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
        result = floor(gross_profit - total_cost)
        # Printing
        # final_result = abs(floor(result))
        # result_str = "de {:,} pratas".format(final_result).replace(',', '.')
        # if result < 0:
        #     print(f"{city}: Prejuízo {result_str}")
        # else:
        #     print(f"{city}: Lucro {result_str}")

        return result
