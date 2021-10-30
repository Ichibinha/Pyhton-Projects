#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np


# In[17]:


Lista = []
Lista.append(int(input('valor\n'))) 
print(Lista)


# In[18]:


#Adicionar mais valores dentro da lista, zerar os que já existiam?
zerar_lista = input('Deseja zerar a lista?\n')
if zerar_lista == 'sim':
    Lista = []
    n_valores= int(input('quantos novos valores gostaria de adicionar?\n'))
    for i in range(n_valores):
        Lista.append(int(input('valor \n'))) 
    print(Lista)    
else:
    n_valores= int(input('quantos novos valores gostaria de adicionar?\n'))
    for i in range(n_valores):
        Lista.append(int(input('Insira o valor \n'))) 
    print(Lista)


# In[20]:


#Média dos valores da lista
Lista_adj = 0
for i in range(len(Lista)):
    Lista_adj = Lista_adj + Lista[i]
Lista_adj = Lista_adj/len(Lista)
Lista_adj


# In[ ]:




