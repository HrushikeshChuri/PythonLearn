#######################################
#   Python Data Types 
# 1. Everything in python is an object derived from class
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
varStringDoubleQuotes = "This is string"

print("varStringDoubleQuotes: ", varStringDoubleQuotes)

print("Type of varStringDoubleQuotes: ", type(varStringDoubleQuotes)) #to check data type of any variable

print("*****************************************************")

#boolean
varBoolean = True  #or False.  Note that T & F are capital
print("varBoolean: ", varBoolean)

print("Type of varBoolean: ", type(varBoolean)) #to check data type of any variable

print("*****************************************************")

########### Sequence Types ##########
varList = [1, 2, 3]

print("varList: ", varList)
print("Type of varList: ", type(varList)) #to check data type of any variable

varTuple = (1, 2, 3)

print("varTuple: ", varTuple)
print("Type of varTuple: ", type(varTuple)) #to check data type of any variable

varRange = range(0, 10)

print("varRange: ", varRange) #we usually do not use range this way. It is used for iteration
print("Type of varRange: ", type(varRange)) #to check data type of any variable

########### Set Types ##########

varSet = { 1, 2, 3}

print("varSet: ", varSet)
print("Type of varSet: ", type(varSet)) #to check data type of any variable

varFrozenset =  frozenset([1, 2, 3])

print("varFrozenset: ", varFrozenset)
print("Type of varFrozenset: ", type(varFrozenset)) #to check data type of any variable

########### Mapping Types ##########

varDictionary = { 'key1': "value1", 'key2': "value2"}

print("varDictionary: ", varDictionary)
print("Type of varDictionary: ", type(varDictionary)) #to check data type of any variable
