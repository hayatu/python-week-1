# While loop = loop untill false , when you dont know the end

# i = 1
# while i < 10:
#     print(i)
#     if i==4:
#         print("Found")
#         break 
#     i +=1

# Continue

# i = 1
# while i < 10:
#     print(i)
#     i+=1
#     print("Found")
#     continue
#  
#Else

# i = 1
# while i <= 5:
#     print(i,"is less than 5")
#     i+=1
#     print("Found")
# else:
#     print(i, "is not in the list")

#For Loop = iterate over sequence (Kusoo celceli waxyaabo)

# fruits =["Apple", "Bananan", "Cherry"]
# for items in fruits :
#     print(items)

# fruits =["Apple", "Bananan", "Cherry"]
# for x in fruits :
#     print(x)
#     if x =="Bananan":
#         print("Found")
#         break 
# fruits =["Apple", "Bananan", "Cherry"]
# for x in fruits :
#     print(x)
#     if x =="Bananan":
#         print("Found")
#         continue 

#Range 

# for x in range(1,20,3):
#          print(x)

#Nested for Loop

# colors  = ["Red","Yellow","Orange"]
# fruits = ["Apple","Banana", "Cherry"]
# for x in colors: 
#     for y in fruits: 
#         print(x,y)

#Enumerate Counter -build in fucntion
fruits = ["Apple","Banana", "Cherry"]
for counter, x in enumerate(fruits) :
    print(counter, x)