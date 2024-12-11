#######################################
# More on strings
# 1. Different types of declaring strings
# 2. Slicing Strings
# 3. String methods
# 4. Escape Characters
#######################################

# 1. Different types of declaring strings *******************************************

varStringSingleQuotes = 'This is also "string"'
varStringDoubleQuotes = "This is 'string'"
varStringThreeQuotes = """This is also 'another' way to define \"string\""""
varStringMultiline1 = """
This is multi line string.
Very useful to increase readability.
Also can be used while defining email message body
"""
varStringMultiline2 = '''
This is multi line string.
Very useful to increase readability.
Also can be used while defining email message body
'''

print("varStringSingleQuotes: ", varStringSingleQuotes)
print("varStringDoubleQuotes: ", varStringDoubleQuotes)
print("varStringThreeQuotes: ", varStringThreeQuotes)
print("varStringMultiline1: ", varStringMultiline1)
print("varStringMultiline2: ", varStringMultiline2)

print("")
print("*********************************************************")
print("")

# F-strings

fStringExample = 35
print(f"You have entered : {fStringExample}. Good Job!")  # Add f infromnt of string to make it F-String

print("")
print("*********************************************************")
print("")

#2. Slicing  ********************************************************************

# Index         0123456789............. 
# Index         .................-3-2-1 

sampleString = "This is a sample string"

'''
    1. Index always start from 0
    2. [start index : end index : step] --> step is optional
'''

print(sampleString[1:5])  #start with index 1 and end with index 5-1 = 4
print(sampleString[:5])  #Start with index 0 and end with index 5-1 = 4
print(sampleString[2:]) #start with index 2 and go till end of the string
print(sampleString[0:100]) #although end index is greater than lenght of string it considers end 

print(sampleString[-5:-2]) #slicing from behind

print(sampleString[1:10:1]) #skipping one character

print(sampleString[::-1])  #reverse whole string

print("")
print("*********************************************************")
print("")

#common string methods
#string is ummutable. it cannot be changed
sampleString2 = " this is new, sample string    "

print(sampleString2.lower())
print(sampleString2.upper())
print(sampleString2.strip())
print(sampleString2.replace("s", "x"))
print(sampleString2.split(","))

print(sampleString2.count("is"))
print(sampleString2.count("is", 0 ,5))
print(sampleString2.count("is", 6, 10))

print(sampleString2.strip().split(","))

print("")
print("*********************************************************")
print("")

#Escape characters
sampleString3 = "This is new, \"sample\" string \nThis is new line.\n Table\tChair\tPen"

print(sampleString3)