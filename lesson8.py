#  Dictionary: unordered, changible, index
#  Making Dicitonary
# student =  {"name" : "Ali", "Email": "abc@gmail.com", "age": 37 }
# # Accessing Key
# # x= student ["Email"]
# x= student.get("name")
# print(x)
# Change item
# student =  {"name" : "Ali", "Email": "abc@gmail.com", "age": 37 }
# student["name"] = "Ahmed"
# print(student)

# How to loop over dictionary

# Print Key
# student =  {"name" : "Ali", "Email": "abc@gmail.com", "age": 37 }

# for x in student: 
#     print (x)

# Print Value
# for x in student: 
#     print (student[x])

# Print both key and value

# student =  {"name" : "Ali", "Email": "abc@gmail.com", "age": 37 }
# for x,y in student.items(): 
#  print(x,y)

# Check if item exists

# student =  {"name" : "Ali", "Email": "abc@gmail.com", "age": 37 }
# if("Email" in student): 
#     print("Yes")
# else:
#     print("No")

# Check lenght of Dict

# student =  {"name" : "Ali", "Email": "abc@gmail.com", "age": 37 }
# print(len(student))

# How to add an Item

# student =  {"name" : "Ali", "Email": "abc@gmail.com", "age": 37 }

# student["Subject"]  = "English"
# print(student)

# How to remove an Item
# student =  {"name" : "Ali", "Email": "abc@gmail.com", "age": 37 }
# student.pop("age")

# student.popitem()  # before Python 3.7, it will remove random
# student.clear() # Empty dict
# print("student", student)

# Nested
# students = {
# "student1" : {
#             "name" : "Ali", 
#             "Email": "abc@gmail.com", 
#             "age": 37 ,
#             "Subject": "English",
#             "enroled" : True
#             },
#             "student2" : {
#             "name" : "Ahmed", 
#             "Email": "ahmedc@gmail.com", 
#             "age": 28,
#             "Subject": "Math",
#             "enrolled" : False
#             }
# }

# Makşng a Nested Dict
student1 = {
            "name" : "Ali", 
            "Email": "abc@gmail.com", 
            "age": 37 ,
            "Subject": "English",
            "enroled" : True
            }

student2 = {
"name" : "Ahmed", 
"Email": "ahmedc@gmail.com", 
"age": 28,
"Subject": "Math",
"enrolled" : False
}
student2 = {
    "student1": student1,
    "student2" : student2
    }
print(student2)