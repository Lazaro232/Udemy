from food import Food
from flask import Flask, render_template, request, url_for, redirect


food = Food()

omelette_t3_dict = food.omelette_t3()
# omelette_t5_dict = food.omelette_t5()
# omelette_t7_dict = food.omelette_t7()

foods = {
    'omelete_t3': omelette_t3_dict,
    # 'omelete_t5': omelette_t5_dict,
    # 'omelete_t7': omelette_t7_dict,
}


app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


@app.route('/food/<food_name>')
def meal(food_name):
    food = foods.get(food_name)

    return render_template('food_result.html', food=food)


if __name__ == '__main__':
    app.run(debug=True)
