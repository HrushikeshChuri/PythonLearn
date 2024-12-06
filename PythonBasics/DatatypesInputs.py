#######################################
#   BASIC Data Types 
#######################################

# int
a_int= 5

#string
b_string = "This is 'string'"
c_string = 'This is also "string"'
d_string = """This is also 'another' way to define \"string\""""
e_string = """
This is multi line string.
Very useful to increase readability.
Also can be used while defining email message body
"""
#boolean
f_boolean = True  #or False.  Note that T & F are capital

#print variables

print("a_int: ", a_int)
print("a_int: " + str(a_int)) #another way to print. Since a_int is not string, need to typecast to string

print("b_string: ", b_string)
print("c_string: ", c_string)
print("d_string: ", d_string)
print("e_string: ", e_string)

print("f_boolean: ", f_boolean)


#Gettig input from user and storing it
user_name = input("Your Name: ")
print("Hello ", user_name) #one way to write variable value to console which we have already seen
print("Hello " + user_name) #another way to write variable value on console which is also seen
print(f"Hello {user_name}") # This is coolest way of all - also called as f-string or formatted strings. 
                            #don't forget to add 'f' in front of string

#Getting input other than string
user_height = float(input("Enter your height (m): ")) #Data type of input is always string

ideal_weight = 25 * (user_height ** 2)

print(f" Hello {user_name}, your age is {str(user_height)} and your ideal weight is {str(ideal_weight)} kg")