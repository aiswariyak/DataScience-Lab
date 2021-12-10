#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Write Python program to create two matrices (read values from user) and find the following

import numpy as np
r=int(input("enter the no of rows of first matrix"))
c=int(input("enter the no of columns of first matrix"))
print("\nenter the matrix elements\n")
entry=list(map(int,input().split()))
arr=np.array(entry).reshape(r,c)
print("\ninput arrays\n",arr)
m=int(input("enter the no of rows of second matrix"))
n=int(input("enter the no of columns of second matrix"))
print("\nenter the matrix elements\n")
entry2=list(map(int,input().split()))
arr1=np.array(entry2).reshape(m,n)
print("\ninput arrays\n",arr1)
#1. Dot Product
print("\ndot product of given matrixes:\n")
print(np.dot(arr,arr1))
#2.transpose
print("\ntranspose of 2 matrices\n",arr.transpose())
print(arr1.transpose())
#3.Trace
print("\ntrace of first matrix:\n",np.trace(arr))
print("\ntrace of second matrix:\n",np.trace(arr1))
#Rank
print("\nrank of first matrix:\n",np.linalg.matrix_rank(arr))
print("\nrank of second matrix:\n",np.linalg.matrix_rank(arr1))
#Determinant
print("\ndeterminant of first matrix:\n",np.linalg.det(arr))
print("\ndeterminant of second matrix:\n",np.linalg.det(arr1))
#Inverse
print("\ninverse of first matrix:\n",np.linalg.inv(arr))
print("\ninverse of second matrix:\n",np.linalg.inv(arr1))
#eigen values and eigen vectors
w, v = np.linalg.eig(arr)
x, y = np.linalg.eig(arr1)
print("\neigen values and eigen vectors of first matrix:\n")
print("\neigen value:\n",w)
print("\neigen vectors:\n",v)
print("\neigen values and eigen vectors of second matrix:\n")
print("\neigen value:\n",x)
print("\neigen value:\n",y)


# ## 

# In[ ]:




