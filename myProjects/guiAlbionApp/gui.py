import tkinter as tk
from tkinter import Checkbutton
from food import Food


# Window
root = tk.Tk()
root.title("Food Calculator")
root.geometry("700x750")
# Frame
frame = tk.Frame(root)
frame.grid(row=12, columnspan=4)


def get_food_string(food_name):
    food_type, tier = food_name.split("_")  # ['stew', 't4']
    food_type_title = food_type.title()  # 'Stew'
    food_tier_title = tier.title()  # T4
    food_str = food_tier_title + ' ' + food_type_title  # T4 Stew
    return food_str


def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()


def print_answers(food_info, food_str):
    clear_frame()
    answer_label = tk.Label(
        frame, text=f"--- {food_str} Results ---", font=("Courier", 30))
    answer_label.grid(row=11, columnspan=4)
    index = 0
    init_row = 12
    init_column = 0
    for city in food_info:
        city_label = tk.Label(
            frame,
            text=f"{city}: {food_info[city]}",
            font=("Arial", 15), pady=30)
        row = init_row + index
        if row == 15:
            row = init_row
            init_column += 2
            index = 0
        column = init_column
        city_label.grid(row=row, column=column)
        index += 1


def food(food_name):
    food = Food()
    amount_to_craft = int(amount.get())
    tax_fee = int(fee.get())
    focus = focus_var.get()
    user_info = [amount_to_craft, tax_fee, focus]
    food_dict = food.all_foods(user_info, food_name)
    food_str = get_food_string(food_name)  # T4 Stew
    print_answers(food_dict, food_str)


# Objects
amount = tk.StringVar()
amount.set("100")
fee = tk.StringVar()
fee.set("50")
focus_var = tk.IntVar()

# Labels
craft_amount = tk.Label(
    root, text="How much to craft (e.g, 100): ", padx=10, pady=10)
tax_fee = tk.Label(
    root, text="Tax fee (e.g, 50) ", pady=30)
empty_label = tk.Label(root, text="")  # Create an empty line
empty_label_1 = tk.Label(root, text="")
# Label grid
craft_amount.grid(row=0, column=0)
tax_fee.grid(row=1, column=0)
empty_label.grid(row=6, columnspan=3)
empty_label_1.grid(row=10, columnspan=4)


# Entries
craft_amount_entry = tk.Entry(
    root, width=15, textvariable=amount, borderwidth=5)
tax_fee_entry = tk.Entry(
    root, width=15, textvariable=fee, borderwidth=5)
# Entry grid
craft_amount_entry.grid(row=0, column=1)
tax_fee_entry.grid(row=1, column=1)

# Checkbox
checkbox = Checkbutton(root, text="Focus",
                       variable=focus_var, font='arial', padx=50)
checkbox.grid(row=0, column=2)

# Omelette Buttons
omelette3_button = tk.Button(
    root, text="T3 Omelette", pady=10,
    command=lambda: food('omelette_t3')).grid(row=3, column=0)
omelette5_button = tk.Button(
    root, text="T5 Omelette", pady=10,
    command=lambda: food('omelette_t5')).grid(row=4, column=0)
omelette7_button = tk.Button(
    root, text="T7 Omelette", pady=10,
    command=lambda: food('omelette_t7')).grid(row=5, column=0)
# Stew Buttons
stew4_button = tk.Button(
    root, text="T4 Stew", padx=22, pady=10,
    command=lambda: food('stew_t4')).grid(row=3, column=1)
stew6_button = tk.Button(
    root, text="T6 Stew", padx=22, pady=10,
    command=lambda: food('stew_t6')).grid(row=4, column=1)
stew8_button = tk.Button(
    root, text="T8 Stew", padx=22, pady=10,
    command=lambda: food('stew_t8')).grid(row=5, column=1)
# Sandwich Buttons
sandwich4_button = tk.Button(
    root, text="T4 Sandwich", padx=28, pady=10,
    command=lambda: food('sandwich_t4')).grid(row=3, column=2)
sandwich6_button = tk.Button(
    root, text="T6 Sandwich", padx=28, pady=10,
    command=lambda: food('sandwich_t6')).grid(row=4, column=2)
sandwich8_button = tk.Button(
    root, text="T8 Sandwich", padx=28, pady=10,
    command=lambda: food('sandwich_t8')).grid(row=5, column=2)
# Roast Buttons
roast3_button = tk.Button(
    root, text="T3 Roast", padx=22, pady=10,
    command=lambda: food('roast_t3')).grid(row=7, column=0)
roast5_button = tk.Button(
    root, text="T5 Roast", padx=22, pady=10,
    command=lambda: food('roast_t5')).grid(row=8, column=0)
roast7_button = tk.Button(
    root, text="T7 Roast", padx=22, pady=10,
    command=lambda: food('roast_t7')).grid(row=9, column=0)
# Pie Buttons
pie3_button = tk.Button(
    root, text="T3 Pie", padx=28, pady=10,
    command=lambda: food('pie_t3')).grid(row=7, column=1)
pie5_button = tk.Button(
    root, text="T5 Pie", padx=28, pady=10,
    command=lambda: food('pie_t5')).grid(row=8, column=1)
pie7_button = tk.Button(
    root, text="T7 Pie", padx=28, pady=10,
    command=lambda: food('pie_t7')).grid(row=9, column=1)
# Salad Buttons
salad2_button = tk.Button(
    root, text="T2 Salad", padx=41, pady=10,
    command=lambda: food('salad_t2')).grid(row=7, column=2)
salad4_button = tk.Button(
    root, text="T4 Salad", padx=41, pady=10,
    command=lambda: food('salad_t4')).grid(row=8, column=2)
salad6_button = tk.Button(
    root, text="T6 Salad", padx=41, pady=10,
    command=lambda: food('salad_t6')).grid(row=9, column=2)
# Soup Buttons
soup1_button = tk.Button(
    root, text="T1 Soup", padx=41, pady=10,
    command=lambda: food('soup_t1')).grid(row=3, column=3)
soup3_button = tk.Button(
    root, text="T3 Soup", padx=41, pady=10,
    command=lambda: food('soup_t3')).grid(row=4, column=3)
soup5_button = tk.Button(
    root, text="T5 Soup", padx=41, pady=10,
    command=lambda: food('soup_t5')).grid(row=5, column=3)


root.mainloop()
