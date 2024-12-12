#######################################
# List and Tuples
#######################################

#   list with different data types
#   Accessing list items
#   Looping and list comprehention  
#   Add/remove/change list items
#   other list methods (len/count, sort/reverse, copy/append/extend, clear/pop/remove, index/insert)

# 1. List with different data types
sampleList = [True, "string1", 3, 4.56]

print(sampleList)
print(type(sampleList))

# 2. Accessing list items

print(sampleList[0])
print(sampleList[1])
print(sampleList[1:3])
print(sampleList[:])
print(sampleList[::-1])

for item in sampleList:
    print(f"{item} is of type {type(item)}")

for index in range(len(sampleList)):
    print(f"{sampleList[index]} has index {index}")

#list comprehension

numberList = list(range(1,21))  #list of number from 0 to 20
print (numberList)

evenNumberList = [x for x in numberList if x % 2 == 0] 

print(evenNumberList)



#Manipulating List
sampleList = [True, "string1", 3, 4.56]

# Add/Modify item(s)
## modify existing item

sampleList[1] = 99
sampleList[2] = "new item"

print(sampleList)

## Add new item at the end
sampleList.append("appended")

print(sampleList)

sampleList.insert(3, "inserted")
print(sampleList)

## Copying to nother list or appending list

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

#   other list methods (len/count)

# Remove items(s)
list3.pop()
print(list3)
list3.remove(2)
print(list3)
list3.clear()
print(list3)



list1 = [1, 2, 3, 3 ,4 ,5 ,4, 4]
print(list1.count(4))
print(len(list1))

#tuple

#tuple is immutable. Cannot modify items in tuple
# accessing tuple elements is same as list

sampleTuple = (1, 2, "string", 4.5, 5)

for item in sampleTuple:
    print(item)

print(sampleTuple[1])

#update tuple -- convert tuple to list --> update list and then convert to tuple

newList = list(sampleTuple)
newList.append("new item")

sampleTuple = tuple(newList)

print(sampleTuple)

#tuple unpacking
sampleTuple = ("1", "2", "3")

x, y, z = sampleTuple

print(f"X: {x}, Y: {y}, Z: {z}")