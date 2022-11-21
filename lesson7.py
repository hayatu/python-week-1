# Sets, unordered, unique, uneditable

# fruits ={"Apple", "Mango", "Banana", "Berry"}

# # Accesing

# for x in fruits:
#     print(x)

# Add to set
# fruits ={"Apple", "Mango", "Banana", "Berry"}
# fruits.add("Orange")

# print(fruits)

# Add multiple items
# fruits ={"Apple", "Mango", "Banana", "Berry"}

# fruits.update(["Grapes","Orange","Melon"])

# print(fruits)

# Remove items

# fruits ={"Apple", "Mango", "Banana", "Berry"}
# # fruits.remove("Berry")

# # fruits.discard("He")

# # fruits.pop()

# fruits.clear()

# print(fruits)
#  How to combine two sets

fruits ={"Apple", "Mango", "Banana", "Berry"}
fruit2  ={"Melon", "Kiwi","Banana"}

# fruit3 = fruits.union(fruit2)
fruits.update(fruit2)
print(fruits)