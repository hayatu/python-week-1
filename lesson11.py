#Funcyion lock of code 
#Basic funtion
# def hassan(): 
#     print("Hello")
#Pass
# def hassan(): 
#     pass

#Arguments
# def salam(name): 
#     print("ASC", name)
# salam("Ali")

# def add(x): 
#    print(10+x)
# add(5)

#Multiple Arguments
# def salam(firs_name, last_name): 
#     print("ASC", firs_name,last_name)
# salam("Ali", "Hasan")

#Arbitrary Arguments
# def mykids(*kids):
#     print("My youngest kid is " +kids[1])
# mykids("Osman", "Ali")

#Keyword Arguments(Kwargs)
# def MyKids(child1, child2):
#     print("My yougest kid is " +child2)
# MyKids(child1="Ali",child2="Osma")

#Arbitrary Keyword Arguments(**Kwargs) - Dict

def kids(**kids):
    print("Her first name is " + kids["first_name"])
    print("Her last name is " + kids["last_name"])
kids(first_name ="Ali", last_name ="Hassan")

#Return Value
# def func1(x,y) :
#     return y*x
# print(func1(7,8))

#Default parameter

# def wadan(wadan = "Somalia"):
#     print("I am from Somalia " + wadan)
# wadan("US")

#Lambda  Function/Expression - Small ANonymous Function
#Lambda  Argument: expression
# x= lambda a: a+10
# print(x(5))

# Multiply
# x =lambda a,b: a*b
# print(x(5,4))

# Power of Lambda function within fucntion
def Myfucn(n) :
    return lambda a: a*n
double = Myfucn(2)
print(double(10))