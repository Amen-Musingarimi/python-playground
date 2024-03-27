available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]

current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("keyboard")
        elif current_choice == "4":
            computer_parts.append("Mouse")
        elif current_choice == "5":
            computer_parts.append("mouse pad")
        elif current_choice == "6":
            computer_parts.append("hdmi cable")

    else:
        print("Please add options from the list below:")
        for index, part in enumerate(available_parts, start=1):
            print("{0}: {1}".format(index, part))

    current_choice = input()

print(computer_parts)
