import tkinter as tk
from tkinter import Checkbutton, Variable, ttk
from food import Food


FOOD_LIST = ["omelette_t3", "omelette_t5", "omelette_t7",
             "stew_t4", "stew_t6", "stew_t8",
             "sandwich_t4", "sandwich_t6", "sandwich_t8",
             "roast_t3", "roast_t5", "roast_t7",
             "pie_t3", "pie_t5", "pie_t7",
             "salad_t2", "salad_t4", "salad_t6",
             "soup_t1", "soup_t3", "soup_t5"]

root = tk.Tk()
root.title("Food Calculator")
root.geometry("600x600")


def print_me(i):
    print(i)


def title(food_name):
    food_type, tier = food_name.split("_")  # ['stew', 't4']
    food_type_title = food_type.title()  # 'Stew'
    tier_title = tier.title()  # T4
    food_str = tier_title + ' ' + food_type_title

    return food_str


# Objects
amount = tk.StringVar()
fee = tk.StringVar()
focus = tk.IntVar()

# Labels
craft_amount = tk.Label(
    root, text="How much to craft (e.g, 100): ", padx=10, pady=10)
tax_fee = tk.Label(root, text="Tax fee (e.g, 50) ", pady=30)
craft_amount.grid(row=0, column=0)
tax_fee.grid(row=1, column=0)

# Entries
craft_amount_entry = tk.Entry(
    root, width=15, textvariable=amount, borderwidth=5)
tax_fee_entry = tk.Entry(
    root, width=15, textvariable=fee, borderwidth=5)
craft_amount_entry.grid(row=0, column=1)
tax_fee_entry.grid(row=1, column=1)

# Checkbox
checkbox = Checkbutton(root, text="Focus", variable=focus, font='arial')
checkbox.grid(row=0, column=2)
# Food Buttons
column = 0
row_offset = 3
row_increment = 0
for i in FOOD_LIST:
    index = FOOD_LIST.index(i)
    text = title(i)

    if index and index % 3 == 0:  # row 5, 8 and 11
        if column and column == 2:
            column = 0
            row_increment += 3
            row = row_offset + row_increment
        else:
            column += 1
            row = row_offset + row_increment
    elif not index:
        row = row_offset
    else:
        row += 1

    button = tk.Button(root, text=text, padx=40, pady=10,
                       command=lambda: print_me(i))
    button.grid(row=row, column=column)

# Run Button
# run_button = tk.Button(root, text="Run", command=print_me,
#                        bg="green", activebackground="green", padx=30, pady=30)

# run_button.grid(column=1)


root.mainloop()
