from content import pantry, recipes

cart_items = []


def add_items_to_cart(item: dict):
    cart_items.append(item)


display_dict = {}
for index, key in enumerate(recipes):
    # print(index, key)
    display_dict[str(index + 1)] = key
# print(display_dict)

while True:
    # Display a menu of the recipes  we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking Ingredients")
        ingredients = recipes[selected_item]
        print(ingredients)

        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if food_item in pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"Your recipe needs {required_quantity} of {food_item}")
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_items_to_cart({food_item: quantity_to_buy})


print(cart_items)
