menu_list = ["Learn Python", "Learn Java", "Go Swimming", "Have Dinner", "Go To Bed"]

print("Please choose your option from the list below:")
for index, option in enumerate(menu_list, start=1):
    print(f"{index}. {option}")

choice = None

while True:
    choice = int(input("Enter the number that correspond to your choice: "))
    if choice == 0:
        print("Exiting the program...")
        break
    elif choice > 5 or choice < 0:
        continue
        
    else:
        print("Good luck, you can go {}".format(menu_list[choice - 1]))

    