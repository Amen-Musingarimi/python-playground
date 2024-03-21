shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None # Note that None represents a variable without a value.It is equvalent to Null in Java, C and JavaScript

for index in range(len(shopping_list)): #Note that len() is a python inbuilt fuction that returns length of the varialbe
  if shopping_list[index] == item_to_find:
    found_at = index
    break #Break is important to break out of the loop when the condition we have set has been met. It prevents the iteration to continue.

print(found_at)
print(shopping_list[found_at])
print(len("Takudzwa"))