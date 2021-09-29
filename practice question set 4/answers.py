# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import random


# generate a random list of size 100
myList = []

for i in range(100):
    myList.append(random.randint(0,100))


# print sum using in built function
print(sum(myList))

# normal method
summ = 0

for i in myList:
    summ = summ + i

print(summ)


# %%
# largest number from the list

# normal method
print(max(myList))

largest = myList[0]

for i in myList:
    if(i > largest):
        largest = i

print(largest)


# %%
tupleList = [('a' , 1) , ('b' , 4) , ('c' , 3)]

# sort list according to last element
sortedList = sorted(tupleList , key=lambda x:x[-1])

print(sortedList)


# %%
# remove duplicates from list

# using sets
mySet = list(set(myList))

print(mySet)


# else
newList = []

for i in myList:
    if(i not in newList):
        newList.append(i)

print(newList)


# %%
wordList = ["hello" , "don" , "john" , "harsh native" , "king" , "oops"]

n = 3

result = []

for i in wordList:
    if(len(i) > n):
        result.append(i)

print(result)


# %%
# difference btw two list


list1 = [1,2,3,4,5,7]
list2 = [2,3,7,8,9]

# using sets
print(list(set(list1) - set(list2)))


# without using sets

result = []

for i in list1:
    if(i not in list2):
        result.append(i)

print(result)


# %%
myDict = {"one" : 1 , "two" : 2 , "three" : 3}

print(myDict)

# adding key = four
myDict["four"] = 4

print(myDict)


# %%
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)

print(dic1)


# %%
# remove dic1 key - 6

del dic1[6]

print(dic1)


# %%
result = 1

for i,j in dic1.items():
    result = result * i * j

print(result)


# %%



