#!/usr/bin/env python
# coding: utf-8

# In[3]:


s = "Hi there Class!"

print(s.split())


# In[4]:


planet = "earth"

diameter = 12742

print("The diameter of the {} is {} kilometers.".format(planet , diameter))


# In[5]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

print(lst[3][1][2])


# In[8]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3]['tricky'][3]['target'][3])


# In[9]:


string = "user@domain.com"

def grabDomain(string):
    myString = ""
    found = False
    for i in string:
        if(found):
            myString = myString + i
            
        if(i == "@"):
            
            found = True
            
    return myString

print(grabDomain(string))
        


# In[11]:


def countFound(string , searchString):
    
    count = 0
    
    for i in range(len(string)):
        if(string[i:i+len(searchString)] == searchString):
            count = count + 1
            
    return count



def foundTrueFalse(string , searchString):
    
    count = countFound(string , searchString)
    
    if(count > 0):
        return True
    else:
        return False


print(foundTrueFalse("cksdog nkjsbak dog" , "dog"))

    


# In[12]:


def countFound(string , searchString):
    
    count = 0
    
    for i in range(len(string)):
        if(string[i:i+len(searchString)] == searchString):
            count = count + 1
            
    return count


print(countFound("cksdog nkjsbak dog" , "dog"))

    


# In[13]:


seq = ['soup','dog','salad','cat','great']

print(list(filter(lambda word:word[0] == 's' , seq)))


# In[16]:


def caugthSpeed(speed):
    if(speed <= 60):
        return "no challan"
    elif(speed <= 80):
        return "small challan"
    elif(speed > 80):
        return "big challan"
    
print(caugthSpeed(60))
print(caugthSpeed(80))


# In[17]:


list1 = ["M", "na", "i", "She"]
list2 = ["y", "me", "s", "lly"]

resultList = []

for i,j in zip(list1 , list2):
    resultList.append(i + j)
    
print(resultList)


# In[18]:


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

resultList = []

for i in list1:
    for j in list2:
        resultList.append(i + j)
        
        
print(resultList)
    


# In[23]:


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2 , 7000)


print(list1)


# In[30]:


list1 = [5, 20, 15, 20, 25, 50, 20]


for i in list1:
    if(i == 20):
        list1.remove(20)
        
        
print(list1)


# In[31]:


d = {'a': 100, 'b': 200, 'c': 300}


for i,j in d.items():
    if(j == 200):
        print(True)
        
        


# In[33]:


# Find the sum of the series 2 +22 + 222 + 2222 + .. n terms


n = int(input("Enter the value of n : "))

sum = 0

for i in range(n):
    
    number  = ""
    for j in range(i+1):
        number = number + "2"
        
    number  = int(number)
    
    sum = sum + number
    
print(sum)


# In[ ]:




