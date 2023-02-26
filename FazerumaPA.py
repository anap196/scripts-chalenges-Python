# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 21:48:04 2020

@author: Ana Paula
"""

a1 = int(input('Digite o primeiro termo da sua PA: '))
razão = int(input('Digite a razão da sua PA: '))
for c in range(1, 10+1):
    pa = a1 + (c - 1) * razão
    print('{}'.format(pa), end=' -> ')
print('Os 10 primeiros termos de uma PA.')

# modo do professor:
'''primeiro = int(input('Digite o primeiro termo da sua PA: '))
razão = int(input('Digite a razão da sua PA: '))
décimo = primeiro + (10 -1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end='-> ')
print('ACABOU')'''
    
    
