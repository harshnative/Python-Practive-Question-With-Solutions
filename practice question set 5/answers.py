# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
myTuple = ("hello" , 123 , 123.45 , b"hello")

print(myTuple)


# %%
# tuple is a immutable object , you need to specific all the elements at the creation time only


# %%
print(str(myTuple))


# %%
myTuple = (1,2,3,4,5,6,7,8,9)

# 4th element from front
print(myTuple[4])

# 4th element from last 
print(myTuple[-4])


# %%
# repeated items in tuple
myTuple = (1,2,4,5,4,6,2,1,35,8)

result = []

for i in set(myTuple):
    iCount = myTuple.count(i)

    if(iCount > 1):
        result.append([i , iCount])

print(result)


# %%
myTuple = (1,2,4,5,4,6,2,1,35,8)


def searchInTuple(toSearch):

    # using index method
    try:
        indexOfElement = myTuple.index(toSearch)
        print("element found at index =" , indexOfElement)
    except ValueError:
        print("element not found")


    print('\n-------------------------\n')

    # using normal searching
    found = False

    for i,j in enumerate(myTuple):
        if(j == toSearch):
            found = True
            print("element found at index =" , i)

    if(not(found)):
        print("element not found")


searchInTuple(4)
print("\n\n________________________\n\n")
searchInTuple(7)    


# %%
myList = [1,2,4,5,54968,415,13,45,6]

myTuple = tuple(myList)

print(myTuple)


# %%
# 2 is inclusive and 4 is exclusive
print(myTuple[2:4])


# %%
print(len(myTuple))


# %%
myList = [
    (1,2,3) , 
    (4,5,6) , 
    (7,8,9)
]

myDict = {}

for i,j in enumerate(myList):
    myDict[i] = j

print(myDict)


# %%



