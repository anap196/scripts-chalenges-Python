# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 17:08:25 2020

@author: Ana Paula
"""


x = int(input('Digite um número:'))
resto = x % 2  # %: pegou o resto da divisão pelo número 2
if resto == 0:
    print('O resto da divisão é {}'.format(resto))
    print('O número {} é par'.format(x))
else:
    print('O número {} é ímpar'.format(x))
print('Muito bem!!!')
