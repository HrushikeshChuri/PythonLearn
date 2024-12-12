#######################################
# Loops and Range
# 1. While Loop
# 2. For Loop
# 3. Break and continue
# 4. Nested Loops
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
    counter += 1

# 4.b Continue

#print only even number

counter = 10

while counter > 0:
    counter -= 1
    if counter % 2 != 0:
        continue
    print(counter)
    
# 5. Nested Loops

#Cartesian products

for x in range (0, 3):
    for y in range(0, 3):
        print(f"({x},{y})") 
