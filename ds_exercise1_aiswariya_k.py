#!/usr/bin/env python
# coding: utf-8

# In[9]:


print("-------------------------------------------------------------------------------------------------------------------")

"""1. Write a NumPy program to create an element-wise comparison
(greater, greater_equal, less and less_equal) of two given arrays.
"""
import numpy as np

arr1=np.array([2,4,6,8])
arr2=np.array([2,3,5,9])
print("input Arrays:",arr1,arr2)
print("comparison--->greater")
print(np.greater(arr1,arr2))
print("comparison--->greater_equal")
print(np.greater_equal(arr1,arr2))
print("comparison--->less")
print(np.less(arr1,arr2))
print("comparison--->less_equal")
print(np.less_equal(arr1,arr2))
print("-------------------------------------------------------------------------------------------------------------------")


# In[13]:


#2: Write a NumPy program to create an array of all the even integers from 30 to 70.
even=np.arange(30,71,2)
print("Array of Even numbers:")
print(even)


# In[16]:


#3.Write a NumPy program to create a 3x3 identity matrix.
arr=np.identity(3)
print("3 X 3 identity matrix")
print(arr)


# In[19]:


#4.Write a NumPy program to create a vector with values from 0 to 20 and change the sign of
#the numbers in the range from 9 to 15.
vector=np.arange(21)
print("vector:",vector)
vector[(vector>=9) & (vector<=15)]*=-1
print("vector after changing the sign of numbers in the range 9 to 15")
print(vector)


# In[20]:


#5.Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal
#equal to 1, 2, 3, 4, 5.
matrix=np.diag([1,2,3,4,5])
print("5 x 5 zero matrix having diagonal elements 1,2,3,4,5 is:")
print(matrix)


# In[23]:


#6.Write a NumPy program to compute sum of all elements, sum of each column and sum of
#each row of a given array.
arr=np.array([[1,3,0],[0,5,7]])
print("\nsum of all elements\n",np.sum(arr))
print("\nsum of each column:\n",np.sum(arr,axis=0))
print("\nsum of each row:\n",np.sum(arr,axis=1))


# In[26]:


#7.Write a NumPy program to save a given array to a text file and load it.
np.savetxt("array1.txt",np.array([[1,2],[3,7],[8,3],[1,5]]),fmt="%d")
data=np.loadtxt("array1.txt",dtype=int)
print("\narray in text file:\n",data)


# In[29]:


#8.Write a NumPy program to check whether two arrays are equal (element wise) or not.
A=np.array([[1,2,4],[3,7,6]])
B=np.array([[1,2,2],[2,7,0]])
if np.array_equal(A,B,equal_nan=False):
    print("\ntwo arrays are equal\n")
else:
    print("\ntwo arrays are not equal\n")


# In[32]:


#9.. Write a NumPy program to create a 4x4 array with random values, now create a new array
#from the said array swapping first and last rows.
rnum=np.random.randint(1,50,size=(4,4))
print("\n4 x 4 array with random values\n",rnum)
print("\nNew array after swapping first and last rows\n")
new=rnum[::-1]
print(new)


# In[38]:


#10.Write a NumPy program to multiply two given arrays of same size element-by-element.
arr1=np.array([[1,2,3],[3,2,0]])
arr2=np.array([[3,4,6],[1,5,0]])
print("\ninput arrays:\n")
print(arr1)
print(arr2)
print("after multiplication of arrays:\n",np.multiply(arr1,arr2))


# In[ ]:




