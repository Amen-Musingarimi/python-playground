available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "mouse mat",
    "6": "hdmi cable"
}

current_choice = None
computer_parts = {}
while current_choice != "0":
    if current_choice in available_parts:
        # Note that `in` checks for the keys in the dictionary not the values.
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # It's already in, so remove it
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Please add options from the list below:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")
