#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = list(map(int, input().split()))

counter = {}
max_cnt, winner = 1, a[0]
for x in a:
    counter[x] = counter.get(x, 0) + 1
    if (counter[x] > max_cnt) or (counter[x] == max_cnt and winner > x):
        max_cnt, winner = counter[x], x
    
print(winner)
