#######################################
# List and Tuples
#######################################

'''
Common operations realted to sequence:
    1. Access single or multiple items from sequence
    2. Traverse through sequence
    3. Check if item is in sequence or not
    4. Manipulating Sequence - Add/Modify/Remove item
    5. Sequence type specific operations (like tuple unpacking)

'''

print("*# 1. List with different data types")

sampleList = [True, "string1", 3, 4.56]

print(sampleList)
print(type(sampleList))

print("")
print("*********************************************************")
print("")

print("*# 2. Accessing single or multiple list items")

print(sampleList[0])
print(sampleList[1])
print(sampleList[1:3])
print(sampleList[:])
print(sampleList[::-1])

for item in sampleList:
    print(f"{item} is of type {type(item)}")

for index in range(len(sampleList)):
    print(f"{sampleList[index]} has index {index}")

print("")
print("*********************************************************")
print("")

print("*# 3. Check if item is present in list or not")

print(3 in sampleList) # check if element is in the list
print(True not in sampleList) # check if element is in list

print("")
print("*********************************************************")
print("")

print("*# 4. List comprehension")

numberList = list(range(1,21))  #list of number from 0 to 20

print (numberList)

evenNumberList = [x for x in numberList if x % 2 == 0] 

print(evenNumberList)

print("")
print("*********************************************************")
print("")

print("*# 5. Manipulating List - Add/Modify Existing Item")

sampleList = [True, "string1", 3, 4.56]

sampleList[1] = 99
sampleList[2] = "new item"

print(sampleList)

## Add new item at the end
sampleList.append("appended")

print(sampleList)

sampleList.insert(3, "inserted")
print(sampleList)

## Copying to another list or appending list

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1
print(list3)
list3 = list1[:]
print(list3)

print(list1.copy())

list3.extend(list2)
print(list3)

list3.reverse()
print(list3)
list3.sort()
print(list3)

print("")
print("*********************************************************")
print("")

print("*# 6. Remove items")

# Remove items(s)
list3.pop()
print(list3)
list3.remove(2)
print(list3)
list3.clear()
print(list3)

print("")
print("*********************************************************")
print("")

print("*# 7. Other list methods (len/count)")

list1 = [1, 2, 3, 3 ,4 ,5 ,4, 4]
print(list1.count(4))
print(len(list1))

print("")
print("*********************************************************")
print("")

print("*# 7. Tuple")

###  Tuple is immutable. Cannot modify items in tuple
# Accessing tuple elements is same as list

sampleTuple = (1, 2, "string", 4.5, 5)

for item in sampleTuple:
    print(item)

print(sampleTuple[1])

print("")
print("*********************************************************")
print("")

print("*# 7.a. Update tuple")

#Convert tuple to new list --> update the new list --> Convert new list to tuple

newList = list(sampleTuple)
newList.append("new item")

sampleTuple = tuple(newList)

print(sampleTuple)

print("")
print("*********************************************************")
print("")

print("*# 7.b. Tuple Unpacking")

sampleTuple = ("1", "2", "3")
x, y, z = sampleTuple
print(f"X: {x}, Y: {y}, Z: {z}")