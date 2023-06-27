#!/usr/bin/env python
# coding: utf-8

# # Q-1 What exactly is [ ]
# 
# Ans-   [ ] this is a empty list .

# 
# # Q-2 In a list of values stored in a variable called spam , how would you assign the value "hello" as the third value ? ( Assume [2,4,6,8,10] are in spam)
# 
# 

# In[1]:


# ans-
spam=[2,4,6,8,10]
spam[2]='hello'
print(spam)


# # let's pretend the spam includes the list['a','b','c','d'] for the next three queries .

# # Q-3 what is value of spam[int(int('3'*2)/11)]?

# In[2]:


spam=['a','b','c','d']
spam[int(int('3'*2)/11)]


# In[3]:


spam


# # Q-4 what is the value of spam[-1]

# In[4]:


spam[-1]


# # Q-5 what is the value of spam[:2]

# In[7]:


spam[:2]


# # let's pretend bacon has the list[3.14,'cat','11',True] for the next three questions
# 

# # Q-6 what is the value of bacon.index('cat')?
# 

# In[8]:


bacon=[3.14,'cat','11','cat',True]


# In[9]:


bacon.index('cat')


# # Q-7 how does bacon.append(99)change the look of the list value in bacon?

# In[11]:


bacon.append(99)


# In[12]:


bacon


# # Q-8 how does bacon.remove('cat') change the look of the list in bacon ?

# In[13]:


bacon.remove('cat')


# In[14]:


bacon


# # Q-9 What are the list concatenation and list replication operators ?

# In[15]:


list1=[1,2,3,4]
list2=[5,6,7,8]
list3=list1+list2
print(list3)


# # Q-10 What is difference between the list methods append() and inset()?

# In[20]:


# in insert we can add items easily at any index 
list1=[1,2,3,4]
list1.insert(4,"hello")
print(list1)


# In[ ]:


# but in append we can at the last index autometic


# # Q-11 What are the two methods for removing items from a list?

# In[30]:


## we can remove items from list with two methdods
# remove , pop 
# in pop autometicaly last index item remove

list1=[1,2,3,4,5]
list1.remove(3)
print(list1)
list2=[1,2,3,4]
list2.pop()


# # Q-12 Describe how list values and string values are identical

# In[31]:


# list values are diffrent from string values 
# list values mutable and string values immutable
# list values store in [ ] 
# string values store in " "


# # Q-13 What's the difference between tuples and lists?
# 

# In[32]:


# tuples are immuatable 
# list are mutable


# # Q-14 How do you type a tuple value that only contains the integer 42?

# In[34]:


tup1=(42)
print(type(tup1))
tup2=(42,)
print(type(tup2))


# # Q-15 How do you get a list values tuple form ? How do you get a tuple values list form

# In[1]:


list=[1,2,3,4]
tuple=tuple(list)
print(tuple)
print(type(tuple))


# In[1]:


tuple=(1,2,3,4)
list=list(tuple)
print(list)
print(type(list))


# # Q-16 Variables that "contain" list values are not necessarily lists themselves . Instead , what do they contain ?

# In[2]:


# list 


# In[ ]:




