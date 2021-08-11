from food import Food
from flask import Flask, render_template, request, url_for, redirect


# food = Food()

# omelette_t3_dict = food.omelette_t3()
# omelette_t5_dict = food.omelette_t5()
# omelette_t7_dict = food.omelette_t7()

# foods = {
#     'omelete_t3': omelette_t3_dict,
# 'omelete_t5': omelette_t5_dict,
# 'omelete_t7': omelette_t7_dict,
# }


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/food/<food_name>')
def meal(food_name):
    food = Food()
    if food_name == 'omelete_t3':
        food_str = 'Tier 3 Omelette'
        omelette_t3_dict = food.omelette_t3()
        return render_template('food_result.html',
                               food=omelette_t3_dict,
                               food_name=food_str)
    elif food_name == 'omelete_t5':
        food_str = 'Tier 5 Omelette'
        omelette_t5_dict = food.omelette_t5()
        return render_template('food_result.html',
                               food=omelette_t5_dict,
                               food_name=food_str)
    elif food_name == 'omelete_t7':
        food_str = 'Tier 7 Omelette'
        omelette_t7_dict = food.omelette_t7()
        return render_template('food_result.html',
                               food=omelette_t7_dict,
                               food_name=food_str)


@app.route('/food/form')
def form():
    return render_template('choose_food.html')


if __name__ == '__main__':
    app.run(debug=True)
