# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:32:43 2020

@author: Ana Paula
"""

print('SEQUENCIA DE FIBONACCI!!!')
n = int(input('Quantos elementos você quer mostrar? '))
a1 = 0
a2 = 1
cont = 3
print('{},{} '.format(a1, a2), end='')
while cont <= n:
   a3 = a1 + a2
   print(',{} '.format(a3), end='')
   a1 = a2       # transiçaõ entre os números;
   a2 = a3
   cont += 1
print('Acabou!')
   
   
