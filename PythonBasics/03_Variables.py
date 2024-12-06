#######################################
#   Variables
# 1. Do not specify variable type. Variable types are inferred at run time
# 2. Allowed chars variable name
#       lower and upper case chars
#       digits (variable name cannot start with digits)
#       underscore (variable name can start with underscore)
# 3. Variable names are case sensitive
#
#######################################

########### Changing value type of variable in single snippet of code #######

#As value of variable changes, so does type
original  = 10 # int type
print("Original:", original)
print("Original Type: ", type(original))

original = "Ten" # str type
print("Changed Variable: ", original)
print("Changed Type: ", type(original))
