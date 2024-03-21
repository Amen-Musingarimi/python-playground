shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# In the following iteration we buy everything in the list
for item in shopping_list:
  print("Please buy {}.".format(item))

print("-" * 60)
# In the following iteration we buy everything in the list excluding "spam"
for item in shopping_list:
  if item != "spam":
    print("(Using not equal. )Please buy {}.".format(item))

print("-" * 60)
# In the following iteration we buy everything in the list excluding "spam" using keyword continue
for item in shopping_list:
  if item == "spam":
    continue

  print("(Using Continue.) Please buy {}.".format(item))