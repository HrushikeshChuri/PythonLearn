#######################################
# Loops and Range
# 1. While Loop
# 2. For Loop
# 3. Break and continue
#######################################

#   1. While Loop

counter = 0

while counter < 10:
    print(counter)
    counter += 1

#  2. For Loop
# Note that second argument number is excluded from range generation.
# range(0,10) will only generate numbers from 0 till 9
 
for counter in range(0,10):
    print(counter)


# 3.a Break

counter = 0

while True:
    if counter > 9:
        break
    print(counter)
    
# 4.b Continue