shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None # Note that None represents a variable without a value.It is equvalent to Null in Java, C and JavaScript

for index in range(len(shopping_list)):
  if shopping_list[index] == item_to_find:
    found_at = index

print(found_at)
print(shopping_list[found_at])