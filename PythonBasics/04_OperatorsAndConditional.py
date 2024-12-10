################################################
#   Operators and Conditional Statements
#   Arithmatic Operators: 
#   + , - , *, /
#   %  - Mod operator to get remainder of division
#   ** - Power/Exponent
#
#**********************************************
#   Comparision Operators
#   ==, != , > , < , >= , <=
#
#**********************************************
#   Logical Operators
#   and, or , not
#
#**********************************************
#   Conditional Statements
#   if .. elif....else
###############################################

####  Arithmatic Operators ###################

a = 94
b = 10

print(f"a: {a}, b: {b}")
print("")

print("a + b (addition):", a+b)
print("a - b (subtraction):", a-b)
print("a * b (multiplication):", a*b)
print("a / b (division):", a/b)
print("a // b (floor division):", a//b) #return integer rounded to lowest value

print("a % b (remainder):", a%b)

print(" Square of a :", a ** 2)

print(" Square root of a :", a ** 0.5)

print("")
print("*********************************************************")
print("")

##########  Comparison Operators ################

a = 10
b = 20

print(f"a: {a}, b: {b}")
print("")

print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)
print("a > b:", a > b)
print("a <= b:", a <= b)
print("a >= b:", a >= b)

print("")
print("*********************************************************")
print("")

##########  Logical Operators ###################

a = 10
b = 20
c = 30

print(f"a: {a}, b: {b}, c: {c}")
print("")

print("a == b or b == c: ", a == b or b == c)
print("a != b and b != c: ", a != b and b != c)
print("not a < b: ", not a < b)

print("")
print("*********************************************************")
print("")

############## Conditional Statements ###########

# Comparison and logic operators are usually used with conditional statements

percentage = int(input("Enter your Percentage: "))

if percentage < 40:
    print("Failed!")
elif percentage >= 40 and percentage < 60:
    print("2nd Class!")
elif percentage >= 60 and percentage < 80:
    print("1st Class!")
elif percentage >= 80 and percentage <= 100:
    print("Distiction!")
else:
    print("Invalid Percentage!")

print("")
print("*********************************************************")
print("")

# short hand if

print("Failed!") if percentage < 40 else print("Passed!")  

# short hand if..else

print("Failed!") if percentage < 40 else print("Distinction!") if percentage > 80 else print("Passed!") 