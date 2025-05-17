#!/usr/bin/env python
# coding: utf-8

# # Recursion in python
# Recursion is the process of defining something in terms of itself.
# ### Python Recursive Function
# In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

# In[19]:


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))


# In[20]:


def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




