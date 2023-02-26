# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:33:02 2020

@author: Ana Paula
"""
from random import randrange
n1 = randrange(0, 10)
n2 = randrange(1, 20)
n3 = randrange(5, 10)
n4 = randrange(10, 15)
n5 = randrange(15, 20)
números = (n1, n2, n3, n4, n5)
print(f'Os 5 números aleatórios gerados são: {números}')
print(f'O maior valor é {max(números)}')
print(f'O menor valor é {min(números)}')

# outro modo de fazer, modo do professor:
'''n = (randrange(1, 10), randrange(1, 10), randrange(1, 10), randrange(1, 10), randrange(1, 10))
print('Os valores sorteados foram: ', end='')
for n in números:
    print(f' {n} ', end='')'''