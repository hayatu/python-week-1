# friends = ['Taylor', 'Alex', 'Pat', 'Eli']
# for friend in friends:
#     print("Hi " + friend)

# print(type("a"));

# from turtle import width

# Length =2
# width =5
# area = Length * width
# print(area)

# base = 5
# height = 3
# area = (base * height)/2

# print(area)

# total = 2048 + 4357+ 97658 + 125 + 8
# files = 5
# average = total / files
# print(" The average size is: " + str(average))

# In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. 
# The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip,
#  the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number.
# bill = 47.28
# tip = bill * 0.15
# total = bill + tip
# share = total/2
# print(" Each person needs to pay: " + str(share))
# This code is supposed to take two numbers, divide one by another so that the result is equal to 1, and display the result on the screen. 
# Unfortunately, there is an error in the code. Find the error and fix it, so that the output is correct.
# numerator = 10
# denominator = 10
# result = 10 / 10
# print(result)

# Combine the variables to display the sentence "How do you like Python so far?" 
# word1 = "How"
# word2 = "do"
# word3 = "you"
# word4 = "like"
# word5 = "Python"
# word6 = "so"
# word7 = "far?"
# print(word1 + word2 , word3, word4, word5, word6, word7 )

# Question 4
# This code is supposed to display "2 + 2 = 4" on the screen, but there is an error.
#  Find the error in the code and fix it, so that the output is correct.

# print("2 + 2 = " + str(2 + 2))

# def greeting(name, department) :
#     print("Welcome " + name )
#     print("You are part of the " +department)
# greeting("Ali", "CIT")
# greeting("Ali", "Software Engineering")

# Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, 
# and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

# def print_seconds(hours, minutes, seconds):
#   print(3600*hours+60*minutes+seconds)

# print_seconds(1,2,3)

# def area_traiangle(base,height, ):
#     return base * height/2
# area_a = area_traiangle(5,4)
# area_b = area_traiangle(7,3)

# sum = area_a + area_b 
# print(" the trainagle area is " + str(sum))

# def get_seconds(hours, minutes, seconds):
#   return 3600*hours + 60*minutes + seconds

# amount_a = get_seconds(2,30,0)
# amount_b = get_seconds(0,45,15)
# result = amount_a + amount_b
# print(result)

# name = "Ali"
# number = len(name)*9 
# print ("Hell " + name + ". Your lucky number is " + str(number)) 

# def lucky_number(name):
#   number = len(name) * 9
#   message = "Hello " + name + ". Your lucky number is " + str(number)
#   return message

# print(lucky_number("Kay"))
# print(lucky_number("Cameron"))

# def lucky_number(name): 
#   number = len(name)* 9
#   print ("Hell " + name + ". Your lucky number is " + str(number)) 

# lucky_number("ali")
# lucky_number("Abdi")

# def month_days(month,days):
#   print(month + " has " + str(days) + " days.")
# month_days("june", "30")
# month_days("july", "31")

# def rectangle_area(base, height):
# 	area = base*height  
# 	print("The area is " + str(area))
# rectangle_area(5,6)

# 1) Complete the function to return the result of the conversion
# def convert_distance(miles):
	# km = miles * 1.6  # approximately 1.6 km in 1 mile

# my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
# my_trip_km = 55* 1.6
# 3) Fill in the blank to print the result of the conversion
# print("The distance in kilometers is " + str(my_trip_km))
# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
# print("The round-trip in kilometers is " + str(my_trip_km*2))
# def is_positive(number):
#   if number > 0:
#       return "Positive"
#   elif number<0:
#       return "Negative"
#   else:
#       return "Zero"
# print(is_positive(-2))

# def number_group(number):
#   if number > 0:
#     return "Positive"
#   elif number < 0:
#     return "Negative"
#   else:
#       return "Zero"

# print(number_group(10)) #Should be Positive
# print(number_group(0)) #Should be Zero
# print(number_group(-5)) #Should be Negative

# def color_translator(color):
# 	if color == "red":
# 		hex_color = "#ff0000"
# 	elif color == "green":
# 		hex_color = "#00ff00"
# 	elif color == "blue":
# 		hex_color = "#0000ff"
# 	else:
# 		hex_color = "unknown"
# 	return hex_color

# print(color_translator("blue")) # Should be #0000ff
# print(color_translator("yellow")) # Should be unknown
# print(color_translator("red")) # Should be #ff0000
# print(color_translator("black")) # Should be unknown
# print(color_translator("green")) # Should be #00ff00
# print(color_translator("")) # Should be unknown

# def exam_grade(score):
# 	if score >= 100 :
# 		grade = "Top Score"
# 	elif score >= 60:
# 		grade = "Pass"
# 	else:
# 		grade = "Fail"
# 	return grade

# print(exam_grade(65)) # Should be Pass
# print(exam_grade(55)) # Should be Fail
# print(exam_grade(60)) # Should be Pass
# print(exam_grade(95)) # Should be Pass
# print(exam_grade(100)) # Should be Top Score
# print(exam_grade(0)) # Should be Fail

# def format_name(first_name, last_name):
# # code goes here
# 	string = ('Name: ' +last_name+", "+first_name)
# 	if first_name =="":
# 		return ("Name: " + last_name)
# 	elif last_name =="":
# 		return("Name: "+ first_name)
# 	elif first_name == "" and last_name == "":
# 		return ""
# 	else:
# 		return string 
# print(format_name("Ella", "Fitzgerald"))
# print(format_name("Adele", ""))
# print(format_name("", "Einstein"))
# print(format_name("", ""))

# def longest_word(word1, word2, word3):
# 	if len(word1) >= len(word2) and len(word1) >= len(word3):
# 		word = word1
# 	elif len(word2) >= len(word1) and len(word2) >= len(word3):
# 		len(word1) <= len(word2) and len(word2) >= len(word3)
# 		word = word2
# 	else:
# 		word = word3
# 	return(word)

# print(longest_word("chair", "couch", "table"))
# print(longest_word("bed", "bath", "beyond"))
# print(longest_word("laptop", "notebook", "desktop"))

# def fractional_part(numerator, denominator):
# 	# Operate with numerator and denominator to 
# # keep just the fractional part of the quotient
# 		if denominator ==  0 or numerator == 0:
# 			return 0

# 		else:
# 			fraction = ((numerator / denominator)-(numerator // denominator))
# 		return  fraction

# print(fractional_part(5, 5)) # Should be 0
# print(fractional_part(5, 4)) # Should be 0.25
# print(fractional_part(5, 3)) # Should be 0.66...
# print(fractional_part(5, 2)) # Should be 0.5
# print(fractional_part(5, 0)) # Should be 0
# print(fractional_part(0, 5)) # Should be 0
# my_variable = 5
# while my_variable < 10 :
# 	print("Hello")
# 	my_variable+=1

# def count_down(start_number):
#   current =3
#   while (current > 0):
#     print(current)
#     current -= 1
#   print("Zero!")

# count_down(3)

# def print_prime_factors(number):
#   # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number = number / factor
#     else:
#       # If it's not, increment the factor by one
#       factor+=1
#   return "Done"

# print_prime_factors(100)
# # Should print 2,2,5,5
# # DO NOT DELETE THIS COMMENT

# def is_power_of_two(n):
#   # Check if the number can be divided by two without a remainder
#   while n % 2 == 0:
#     n = n / 2
#   # If after dividing by two the number is 1, it's a power of two
#   if n == 1:
#     return True
#   return False
  

# print(is_power_of_two(3)) # Should be False
# print(is_power_of_two(1)) # Should be True
# print(is_power_of_two(8)) # Should be True
# print(is_power_of_two(9)) # Should be False

# def sum_divisors(n):
#   i =1
#   sum = 0
#   # Return the sum of all divisors of n, not including n
#   for i in range (i, n):
#     if n % i == 0 and i < n:
#       sum += i
#   else:
#     i += 1
#   return sum

# print(sum_divisors(0))
# # 0
# print(sum_divisors(3)) # Should sum of 1
# # 1
# print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# # 114

# def sum_divisors(n):
#   i =1
#   sum = 0
#   # Return the sum of all divisors of n, not including n
#   for i in range (i, n):
#     if n % i == 0 and i < n:
#       sum += i
#   else:
#     i += 1
#   return sum

# print(sum_divisors(0))
# # 0
# print(sum_divisors(3)) # Should sum of 1
# # 1
# print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# # 114

# for x in range(5) :
# 	print(x)

# def square(n):
#     return n*n

# def sum_squares(x):
#     sum = 0
#     for n in range(x):
#         sum += int(square(n))
#     return sum

# print(sum_squares(10)) # Should be 285

# values  = [12,3,6,7,8,0]
# sum = 0
# length = 0
# for value in values:
# 	sum+=value
# 	length+=1
# 	print("Total sum is " +str(sum) + " - Average " + str(sum/length)) 


# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result= result * i
#     return result
# print(factorial(4)) # should return 24
# print(factorial(5)) # should return 120
 			
# def validate_users(users):
#   for user in users:
#     if is_valid(user):
#       print(user + " is valid")
#     else:
#       print(user + " is invalid")

# validate_users(['taylor', 'luisa', 'jamaal'])

# def double_word(word):
#     return word + word + str(len(word) * 2)

# print(double_word("hello")) # Should return hellohello10
# print(double_word("abc"))   # Should return abcabc6
# print(double_word("hello"))      # Should return 0

# def first_and_last(message):
#     if len(message)==0 or message[-1]==message[0]:
#         return True
#     else:
#       return False

# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))
# Answer ="YES"
# if Answer.lower() == "yes":
#       print("the user answered yes")
# def initials(phrase):
#     words = phrase.split()
#     result = ""
#     for word in words:
#         result += word[0].upper()
#     return result

# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS

# name = "Ali"
# number = len(name)*3 
# print("Your lucky number is  {number}, {name}.".format(name=name, number= len(name)*3))
# (80*100)/100

# def student_grade(name, grade):
# 	return "{} received {}% on the exam".format(name, grade)

# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))

# price = 7.5
# with_text = price *1.09
# print(price, with_text)

# print("Base price :${:.2f}. with tax : ${:.2f}" .format(price,with_text))

# def to_celsius(x):
#     return (x-32)*5/9
    
# for x in range(0,101,10):
#             print("{:>3} F| {:>6.2f} C".format(x,to_celsius(x)))

# "base string with {} placeholders".format(variables)

# example = "format() method"

# formatted_string = "this is an example of using the {} on a string".format(example)

# print(formatted_string)

# "{0} {1}".format(first, second)

# first = "apple"
# second = "banana"
# third = "carrot"

# formatted_string = "{0} {2} {1}".format(first, second, third)

# print(formatted_string)


# The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. 
# Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". 
# Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.

# def is_palindrome(input_string):
# 	# We'll create two strings, to compare them
# 	new_string = ""
# 	reverse_string = ""
# 	# Traverse through each letter of the input string
# 	for string in input_string.lower():
# 		# Add any non-blank letters to the 
# 		# end of one string, and to the front
# 		# of the other string. 
# 		if  string != " ":
# 			new_string += string.lower()
# 			reverse_string = string.lower() +reverse_string
# 	# Compare the strings
# 	if new_string==reverse_string:
# 		return True
# 	return False

# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

# Question 2
# Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. 
# For example, convert_distance(12) should return "12 miles equals 19.2 km".

# def convert_distance(miles):
# 	km = miles * 1.6 
# 	result = "{:} miles equals {:.1f} km".format(miles,km)
# 	return result

# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

# def nametag(first_name, last_name):
# 	return("{}{}.".format(first_name,last_name[0]))

# print(nametag("Jane", "Smith")) 
# # Should display "Jane S." 
# print(nametag("Francesco", "Rinaldi")) 
# # Should display "Francesco R." 
# print(nametag("Jean-Luc", "Grand-Pierre")) 
# # Should display "Jean-Luc G."

# def replace_ending(sentence, old, new):
# 	# Check if the old string is at the end of the sentence 
# 	if sentence.endswith(old):
# 		# Using i as the slicing index, combine the part
# 		# of the sentence up to the matched string at the 
# 		# end with the new string
# 		i = sentence.rindex(old)
# 		new_sentence = sentence[:i]+new
# 		return new_sentence

# 	# Return the original sentence if there is no match 
# 	return sentence
	
# print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april")) 
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April")) 
# # Should display "The weather is nice in April"

# def get_word(sentence, n):
# 	# Only proceed if n is positive 
# 	if n > 0:
# 		words = sentence.split()
# 		# Only proceed if n is not more than the number of words 
# 		if n <= len(words):
# 			return(words[n-1])
		
# 	return("")

# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5)) # Nothing

# fruits = ["Aple", "Mango", "Banana"]
# fruits.append("Kiwi")
# print(fruits)
# fruits.insert(0,"Melon")
# print(fruits)
# fruits.remove("Aple")
# print(fruits)
# fruits.pop(2)
# print(fruits)
# fruits[2] = "Apple"
# print(fruits)

# def skip_elements(elements):
#   # Initialize variables
#   new_list = []

#   # Iterate through the list by index
#   for i in range(len(elements)):
#       # Does this element belong in the resulting list?
#       if i % 2 == 0:
#           # Add this element to the resulting list (value at index)
#           new_list.append(elements[i])

#   return new_list

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be 
# ['Orange', 'Strawberry', 'Peach']
# print(skip_elements([])) # Should be []

# def skip_elements(elements):
# 	# Initialize variables
# 	new_list = []
# 	i = 0

# 	# Iterate through the list
# 	for i in range(len(elements)):
# 		# Does this element belong in the resulting list?
# 		if i % 2 == 0:
# 			# Add this element to the resulting list
# 			new_list.append(elements[i])
# 		# Increment i
# 		i+= 1

# 	return new_list

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements([])) # Should be []

# def file_size(file_info):
# 	name, type, size= file_info
# 	return("{:.2f}".format(size/ 1024))

# print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
# print(file_size(('Notes', 'txt', 496))) # Should print 0.48
# print(file_size(('Program', 'py', 1239))) # Should print 1.21

# animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
# chars = 0 
# for animal in animals: 
# 	chars += len(animal) 
# 	print("Total Characters : {}, Average lenght : {}".format(chars, chars/len(animals)))

# winers  = ["Ali", "Abdi", "Farah"]
# for index, person in enumerate(winers):
# 	print("{} - {}".format(index+1, person))

# def full_emails(people):
# 	result=[]
# 	for email, name in people: 
# 		result.append("{} <{}>".format(name, email))
# 	return result
# print(full_emails([("ali@yahoo.com","ali"),("abdi@gmail.com", "Abdi")]))

# def skip_elements(elements):
# 	# code goes here
#   new_elements = []
#   length = len(elements)
  
#   for i in range(0, length, 2):
#     new_elements.append(elements[i])
#   return new_elements

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements([])) # Should be []
# languages = ["P","C", "Java", "Go", "Perl","Ruby"]
# lenghts	= [len(languages) for langauge in languages]
# print(lenghts)

# z = [x for x in range(0,101) if x%3  == 0 ]
# print(z)

# def odd_numbers(n):
# 		return [x for x in range(1,n+1)if x%2==1]

# print(odd_numbers(5))  # Should print [1, 3, 5]
# print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
# print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
# print(odd_numbers(1))  # Should print [1]
# print(odd_numbers(-1)) # Should print []

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# newfilenames =[]
# for filename in filenames:
#     if filename.endswith(".hpp"):
#         filename=filename.replace(".hpp",".h")
#         newfilenames.append(filename)
#     else:
#         newfilenames.append(filename)  

# print(newfilenames) 
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# def pig_latin(text):
#   say = []
#   # Separate the text into words
#   words = text.split()
#   for word in words:
#     # Create the pig latin word and add it to the list
#     word = word[1:] + word[0] + "ay"
#     say.append(word)
#     # Turn the list back into a phrase
#   return " ".join(say)

# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"

# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# def octal_to_string(octal): 
#     result = "" 
#     value_letters = [(4,"r"),(2,"w"),(1,"x")] 
#     #Iterating over each digit in octal 
#     for digit in [int(n) for n in str(octal)]: 

#         #Checking for each of permission values 
#         for value, letter in value_letters: 
#             if digit >= value: 
#                 result += letter 
#                 digit -= value 
#             else: 
#                 result += "-" 
#     return result 
    
# print(octal_to_string(755)) # Should be rwxr-xr-x
# print(octal_to_string(644)) # Should be rw-r--r--
# print(octal_to_string(750)) # Should be rwxr-x---
# print(octal_to_string(600)) # Should be rw-------

# file_counts = {"jpg" :10, "text":14, "cv":2,"py":23}
# print(file_counts["text"])

# file_counts["abc"] =8
# print(file_counts)
# file_counts["cv"] =17
# print(file_counts)
# del file_counts["py"]
# print(file_counts)

# toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# toc["Epilogue"] = 39 # Epilogue starts on page 39
# toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
# print(toc) # What are the current contents?
# print("Chapter 5" in toc) # Is there a Chapter 5?

# file_counts = {"jpg":10, "text" :5, "cvs" :12, "py":20}
# print(file_counts)
# print(file_counts["text"])
# print("jpg" in file_counts)
# file_counts["abc"] =8
# print(file_counts)
# file_counts["cvs"] = 19
# print(file_counts)

# Iterating over the Contents of a Dictionary

# file_counts = {"jpg":10, "text" :5, "cvs" :12, "py":20} 
# for extention in file_counts:
# 	print(extention)

# for ext, amount in file_counts.items():
# 	print("There are {} files with the .{} extention" .format(amount,ext))
# print(file_counts.keys())
# print(file_counts.values())

# for value in file_counts.values():
# 	print(value)

# cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
# for value,amount in cool_beasts.items():
#     print("{} have {}".format(value,amount))

# def count_letters(text) :
# 	result = {}
# 	for letter in text:
# 		if letter not in result:
# 			result[letter] =0
# 			result[letter] += 1
# 	return result

# print(count_letters("aaaa"))
# print(count_letters("tenant"))
# print(count_letters("a long string with a lot of letters"))

# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for cloths,colors in wardrobe.items():
# 	for color in colors:	
# 		print("{} {}".format(cloths,color))

# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for cloths, colors in wardrobe.items():
#     for color in colors:
#         print("{} {}".format(color, cloths))

# def groups_per_user(group_dictionary):
# 	user_groups = {}
# 	# Go through group_dictionary
# 	for group, users in group_dictionary.items():
# 		# Now go through the users in the group
# 		for user in users:
# 			user_groups[user] = user_groups.get(user,[]) + [group]
# 			# Now add the group to the the list of
# # groups for this user, creating the entry
# # in the dictionary if necessary

# 	return(user_groups)

# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))

# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# new_items = wardrobe.update(new_items)

# print(new_items)

# def add_prices(basket):
# 	# Initialize the variable that will be used for the calculation
# 	total = 0
# 	# Iterate through the dictionary items
# 	for items in basket.values():
# 		# Add each price to the total calculation
# 		# Hint: how do you access the values of
# 		# dictionary items?
# 		total +=items
# 	# Limit the return value to 2 decimal places
# 	return round(total, 2)  

# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
# 	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

# print(add_prices(groceries)) # Should print 28.44

# def format_address(address_string):
#   # Declare variables
# 		house_number = ""
# 		street_name = ""
#   # Separate the address string into parts
# 		address_string = address_string.split()
#   # Traverse through the address parts
# 		for number in address_string:
#     # Determine if the address part is the
# 			if number.isdigit():
					
#     # house number or part of the street name
# 					house_number = number
#   # Does anything else need to be done 
#   # before returning the result?
# 			else:
# 				street_name += number
# 				street_name += " "
  
#   # Return the formatted string  
# 		return "house number {} on street named {}".format(house_number, street_name)

# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"

# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"

# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"

# def highlight_word(sentence, word):
# 	return(sentence.replace(word,word.upper()))
# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))

# def combine_lists(list1, list2):
#   # Generate a new list containing the elements of list2
#   # Followed by the elements of list1 in reverse order
#   new_list = list2
#   for i in reversed(range(len(list1))):
#     new_list.append(list1[i])
#   return new_list
	
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

# print(combine_lists(Jamies_list, Drews_list))


# def car_listing(car_prices):
#   result = ""
#   for cars in car_prices:
#     result += "{} costs {} dollars".format(cars,car_prices[cars]) + "\n"
#   return result

# print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# def combine_guests(guests1, guests2):
#   # Combine both dictionaries into one, with each key listed 
#   # only once, and the value from guests1 taking precedence
#   guests2.update (guests1)
#   return guests2
# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

# print(combine_guests(Rorys_guests, Taylors_guests))

# def count_letters(text):
#   result = {}
#   text = text.lower()
#   # Go through each letter in the text
#   for letter in text:
#     # Check if the letter needs to be counted or not
#     if letter .isalpha() and letter not in result:
#         result[letter] = text.lower().count(letter)
#     # Add or increment the value in the dictionary
#   return result

# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}

# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

# class Apple:
#   color = "red"
#   flovor = "sweeet"
# AccessClass = Apple()
# AccessClass.color = "red"
# AccessClass.folover = "sweet"
# print(AccessClass.color)
# print(AccessClass.flovor)
# print(AccessClass.color.upper())

# class Flower:
#   color = 'unknown'

# rose = Flower()
# rose.color = 'Red'

# violet = Flower()
# violet.color ='blue'

# this_pun_is_for_you = Flower()

# print("Roses are {},".format(rose.color))
# print("violets are {},".format(violet.color))
# print(this_pun_is_for_you) 

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

# class Person:
#     apples = 0
#     ideas = 0

# johanna = Person()
# johanna.apples = 1
# johanna.ideas = 1

# martin = Person()
# martin.apples = 2
# martin.ideas = 1

# def exchange_apples(you, me):
# #Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results. 
# #We're going to have Martin and Johanna exchange ALL their apples with #one another.
# #Hint: how would you switch values of variables, 
# #so that "you" and "me" will exchange ALL their apples with one another?
# #Do you need a temporary variable to store one of the values?
# #You may need more than one line of code to do that, which is OK. 
#     x=0
#     x=you.apples
#     you.apples=me.apples
#     me.apples=x
#     return you.apples, me.apples
    
# def exchange_ideas(you, me):
#     #"you" and "me" will share our ideas with one another.
#     #What operations need to be performed, so that each object receives
#     #the shared number of ideas?
#     #Hint: how would you assign the total number of ideas to 
#     #each idea attribute? Do you need a temporary variable to store 
#     #the sum of ideas, or can you find another way? 
#     #Use as many lines of code as you need here.
#     x=0
#     x=you.ideas
#     you.ideas += me.ideas
#     me.ideas += x
    
#     return you.ideas, me.ideas

# exchange_apples(johanna, martin)
# print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
# exchange_ideas(johanna, martin)
# print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# # define a basic city class
# class City:
#     name = ""
#     country = ""
#     elevation = 0
#     population = 0
# # create a new instance of the City class and
# # define each attribute
# city1 = City()
# city1.name = "Cusco"
# city1.country = "Peru"
# city1.elevation = 3399
# city1.population = 358052
# # create a new instance of the City class and
# # define each attribute
# city2 = City()
# city2.name = "Sofia"
# city2.country = "Bulgaria"
# city2.elevation = 2290
# city2.population = 1241675

# # create a new instance of the City class and
# # define each attribute
# city3 = City()
# city3.name = "Seoul"
# city3.country = "South Korea"
# city3.elevation = 38
# city3.population = 9733509
# def max_elevation_city(min_population):
# # Initialize the variable that will hold
# # the information of the city with
# # the highest elevation
#     return_city = City()
# # Evaluate the 1st instance to meet the requirements:
# # does city #1 have at least min_population and
# # is its elevation the highest evaluated so far?
#     if city1.population >= min_population and city1.elevation > return_city.elevation:
#         return_city = city1
# # Evaluate the 2nd instance to meet the requirements:
# # does city #2 have at least min_population and
# # is its elevation the highest evaluated so far?
#     if city2.population >= min_population and city2.elevation >return_city.elevation:
#         return_city = city2
# # Evaluate the 3rd instance to meet the requirements:
# # does city #3 have at least min_population and
# # is its elevation the highest evaluated so far?
#     if city3.population >= min_population and city3.elevation > return_city.elevation:
#         return_city = city3
# #Format the return string
#     if return_city.name:
#         return "{}, {}".format(return_city.name, return_city.country)
#     else:
#         return ""

# print(max_elevation_city(100000)) # Should print "Cusco, Peru"
# print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000)) # Should print ""


# class Furniture:
# 	color = ""
# 	material = ""

# table = Furniture()
# table.color = "brown"
# table.material = "wood"

# couch = Furniture()
# couch.color = "red"
# couch.material = "leather"


# def describe_furniture(piece):
# 	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

# print(describe_furniture(table)) 
# # Should be "This piece of furniture is made of brown wood"
# print(describe_furniture(couch)) 
# # Should be "This piece of furniture is made of red leather"

# class Piglet: 
# 	def speak(self):
# 		print("Oink Oink")
# hamlet = Piglet()
# hamlet.speak()

# class Piglet :
# 	name = "Piglet"
# 	def speak(self):
# 		print("Oink! I'm {}! Oink!". format(self.name))

# halmet = Piglet()
# halmet.name  = "Halmet"
# halmet.speak()
# Petunia =Piglet()
# Petunia.name ="Petunia"
# Petunia.speak()


# class Piglet():
# 	years = 0 
# 	def pig_years(self):
# 		return self.years * 18

# piggy =Piglet()
# print(piggy.pig_years())
# piggy.years = 2
# print(piggy.pig_years())

# class Dog:
#   years = 0
#   def dog_years(self):
# 	  return self.years * 7    
# fido=Dog()
# fido.years=3
# print(fido.dog_years())

class Apple: 
  def __init__(self,color, flavor):
      self.colro = color 
      self.flavor = flavor 

jonagold = Apple("color", "Sweet")
print(jonagold.colro)

