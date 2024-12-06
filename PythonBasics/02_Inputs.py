#######################################
#   Inputs from user
#######################################

#Input as string
user_name = input("Your Name: ")
print("Hello ", user_name) #one way to print variable which we have already seen
print("Hello " + user_name) #another way to print variable which we have already seen
print(f"Hello {user_name}") # This is coolest way of all - also called as f-string or formatted strings. 
                            #don't forget to add 'f' in front of string

print("*****************************************************")

#Getting input other than string
user_height = float(input("Enter your height (m): ")) #Data type of input is always string

ideal_weight = 25 * (user_height ** 2)

print(f" Hello {user_name}, your age is {str(user_height)} and your ideal weight is {str(ideal_weight)} kg")

print("*****************************************************")