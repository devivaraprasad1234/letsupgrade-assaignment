# -*- coding: utf-8 -*-
"""letsupgrade2ndwork.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Un3Sk_V6wv4LBDEm5eITunP9w2zwbF9h
"""

# making a lottery system using python

import random
N=int(input ("enter the number of people in lottery:"))
list=[]
for i in range(N):
 s=input("enter a name:")
 list.append(s)
r=random.randint(0,N-1)
print("the winner of the lottery:",list[r])