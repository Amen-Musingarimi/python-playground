computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]

another_list = computer_parts

print(id(computer_parts))
print(id(another_list))

computer_parts += ["mouse pad"]
print(computer_parts)

print(id(computer_parts))

print(another_list)

a = b = c = d = e = f = computer_parts
print(a)

print("Adding Headphones")

d.append("headphones")
print(f)
print(e)