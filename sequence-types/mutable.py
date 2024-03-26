computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]

another_list = computer_parts

print(id(computer_parts))
print(id(another_list))

computer_parts += ["mouse pad"]
print(computer_parts)

print(id(computer_parts))