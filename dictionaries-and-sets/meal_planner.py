from content import pantry, recipes

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
        print(selected_item)