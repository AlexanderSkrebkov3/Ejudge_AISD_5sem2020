#!/usr/bin/env python
# coding: utf-8

# In[16]:


import random
def quicksort(A):
    b = []
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A) #выбираем опорным случайый элемент
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem) 
            elif elem > q: 
                R.append(elem) 
            else: 
                M.append(elem)
    b = quicksort(L) + M + quicksort(R)    
            
    return b
a = list(map(int, input().split()))
quicksort(a)
#print(quicksort(a))
a = quicksort(a)
for i in a:
    print(i, end=' ')
