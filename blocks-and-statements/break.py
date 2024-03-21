shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# In the following iteration we buy everything in the list excluding "spam" using keyword continue
for item in shopping_list:
  if item == "spam":
    continue

  print("(Using Continue.) Please buy {}.".format(item))

# In the following iteration we buy everything before "spam" and break
for item in shopping_list:
  if item == "spam":
    break

  print("(Using Break.) Please buy {}.".format(item))