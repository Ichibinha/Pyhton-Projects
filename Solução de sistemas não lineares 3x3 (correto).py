#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import numpy as np
import matplotlib.pyplot as plt
import simpy as sp
from numpy import linalg as LA
from numpy.linalg import inv


# In[8]:


x0 = [2,2,0]
x = x0[0]
y = x0[1]
z = x0[2]
eps = 10**(-3)
s = [0, 0, 0]
inter = 0


# Professor, eu não sei se você lê os programas. Mas, o método estava dando errado, pois na equação 3 
# eu tinha deixado no formato em que z é negativo, e por isso o método estava divergindo.
# Por quê isso acontece?
def F(lx, ly, lz):
    b = [0, 0, 0]
    b[0] = lx**2 + ly**2 + lz**2 - 4
    b[1] = (9/2)*(lx**2 + lz**2) + ly**2 - 9
    b[2] = lz - math.sqrt(10/7) * math.sin((math.pi/2)*(ly-math.sqrt(18/7)+1))

    return b

def J_f(lx, ly, lz):
    A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    A[0][0] = 2*lx
    A[0][1] = 2*ly
    A[0][2] = 2*lz
    A[1][0] = 9*lx
    A[1][1] = 2*ly
    A[1][2] = 9*lz
    A[2][0] = 0
    A[2][1] = math.sqrt(10/7)* (math.pi/2) * math.cos((math.pi/2)*(ly-math.sqrt(18/7)+1))
    A[2][2] = 1     
    
    return A     

Normas = 10
Normaf = 10
while (inter<30) and (Normas>eps or Normaf>eps) and (Normas<10**3 or Normaf<10**3):
    
    J = J_f(x, y, z)
    J = np.array(J)                                      
    b = F(x, y, z)
    b = np.array(b)
    s = LA.solve(J, -b)
    #if inter == 0:
       # print(J, b, s)
    xk = x0 + s
    
    Normas = LA.norm(s, np.inf)
    Normaf = LA.norm(b, np.inf)
    
    inter = inter + 1
    x = xk[0]
    y = xk[1]
    z = xk[2]
    x0 = xk
    
print('interações:', inter)
print('(x, y, z):', round(x, 5), round(y,5), round(z,5))
print('Precisão:', round(Normaf,5))


# In[ ]:




