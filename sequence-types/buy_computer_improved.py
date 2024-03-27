available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]

valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

print(valid_choices)
current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)

    else:
        print("Please add options from the list below:")
        for index, part in enumerate(available_parts, start=1):
            print("{0}: {1}".format(index, part))

    current_choice = input()

print(computer_parts)
