# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:48:09 2020

@author: Ana Paula
"""

print('Os fogos de artifício irão começar em breve!!!')
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[37m''Vejam o céu, está muito lindo!!!\033[m')