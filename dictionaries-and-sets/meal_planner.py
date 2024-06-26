from content import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """
    Add a dictionary containing an item and its required quantity to the `shopping` list
    :param amount: An `int` representing quantity of food items
    :param data: A `dict` of shopping items
    :param item: A `string` of food item name
    """
    if item in data:
        data[item] += amount
    else:
        data[item] = amount


display_dict = {}
for index, key in enumerate(recipes):
    # print(index, key)
    display_dict[str(index + 1)] = key
# print(display_dict)

shopping_list = {}

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
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for shopping_item in shopping_list.items():
    print(shopping_item)
