# list : collection , ordered, changible, duplicate

# fruit = ["Mango","Apple", "Grapes"]
# print(fruit[2])

#  Slicing 
# fruit = ["Mango","Apple", "Grapes","Mango","Apple1", "Grapes1","Mango1","Apple2", "Tomato"]
# print(fruit[-4:-1])
#  Change Item
# fruit = ["Mango","Apple", "Grapes","Mango", "Tomato"]

# fruit[1] ="Kiwi"
# print(fruit)

# For loop
# fruit = ["Mango","Apple", "Grapes","Mango", "Tomato"]

# for index, x in enumerate(fruit) :
#     print (index,x)
# If item exists

# fruit = ["Mango","Apple", "Grapes","Mango", "Tomato"]
# if "Banana" in fruit : 
#     print("Yes Mango in list")
# else:
#     print("no")

# fruit = ["Mango","Apple", "Grapes","Mango", "Tomato"]
# print(len(fruit))

#  add item to list  
# fruit = ["Mango","Apple", "Grapes","Mango", "Tomato"]
# fruit.append("Baana")
# fruit.insert(0, "Banana")
# print(fruit.index("Apple"))
# fruit1 = ["Kiwi", "Melon"]
# fruit.extend(fruit1)
# print(fruit+fruit1)

# how to remove

# fruit = ["Mango","Apple", "Grapes","Mango", "Tomato"]
# fruit.remove("Mango")
# RemovedItem = fruit.pop()
# print(RemovedItem)

# Reverse lsit
# numbers =[2,4,8,9,6]
# fruit = ["Mango","Apple", "Grapes","Mango", "Tomato"]
# numbers.sort(reverse =True)
# print(fruit)
# Sorted lsit
# numbers.sort()
# print (numbers)
# SortedNumbers = sorted(numbers)
# print (SortedNumbers)
# Min, Max, Sum
# numbers =[2,4,8,9,6]
# print (sum(numbers))

# Make list String

fruit = ["Mango","Apple", "Grapes","Mango", "Tomato"]

fruit_Str = "," .join(fruit)
fruit_list = fruit_Str.split(" ,")
print(fruit_list) 