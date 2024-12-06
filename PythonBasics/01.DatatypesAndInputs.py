#######################################
#   Python Data Types 
# 1. Everything is object
# 2. Do not specify variable type. Variable types are inferred at run time
# 3. Allowed chars variable name
#       lower and upper case chars
#       digits (variable name cannot start with digits)
#       underscore (variable name can start with underscore)
# 4. Variable names are case sensitive
#
# Basic Data types: int, float, bool
# Sequence Type: list, tuple, range, string (str)
# Set: set, frozenset
# Mapping: dictionary (dict) 
# 
###################### 
# Mutable Types: List, Set, Dictionary (values can be modified using index)
# Immutable type: Bool, Int, Float, Str, Tuple, Frozenset
#######################################

########### BASIC Data Types ##########

# int
varInt= 5

print("varInt: ", varInt)
print("varInt: " + str(varInt)) #another way to print. Since varInt is not string, need to typecast to string
print("Type of varInt: ", type(varInt)) #to check data type of any variable

print("*****************************************************")

#float
varFloat = 1.75

print("varFloat: ", varFloat)
print("Type of varFloat: ", type(varFloat)) #to check data type of any variable

print("*****************************************************")

#string
varStringDoubleQuotes = "This is 'string'"
varStringSingleQuotes = 'This is also "string"'
varStringThreeQuotes = """This is also 'another' way to define \"string\""""
varStringMultiline = """
This is multi line string.
Very useful to increase readability.
Also can be used while defining email message body
"""

print("varStringSingleQuotes: ", varStringSingleQuotes)
print("varStringDoubleQuotes: ", varStringDoubleQuotes)
print("varStringThreeQuotes: ", varStringThreeQuotes)
print("varStringMultiline: ", varStringMultiline)

print("Type of varStringSingleQuotes: ", type(varStringSingleQuotes)) #to check data type of any variable

print("*****************************************************")

#boolean
varBoolean = True  #or False.  Note that T & F are capital
print("varBoolean: ", varBoolean)

print("Type of varBoolean: ", type(varBoolean)) #to check data type of any variable

print("*****************************************************")

########### Sequence Types ##########
varList = [1, 2, 3]

varTuple = (1, 2, 3)

varRange = range(0, 10)

########### Set Types ##########

varSet = { 1, 2, 3}

varFrozenset = { [1, 2, 3] }

########### Mapping Types ##########

varDictionary = { key1: "value1", key2: "value2"}

########### Get Input from user #######

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

########### CHanging value types of variable #######

#As value of variable changes, so does type
original  = 10 # int type
print("Original:", original)
print("Original Type: ", type(original))

original = "Ten" # str type
print("Changed Variable: ", original)
print("Changed Type: ", type(original))

