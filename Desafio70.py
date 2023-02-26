# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:40:13 2020

@author: Ana Paula
"""

tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')),
         int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'Guardando os valores, temos: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 aparece pela primeira vez na {tupla.index(3)+1}ª posição.')
else:
    print('O número 3 não aparece nenhuma vez.')
print('Os valores pares são: ', end='')
for t in tupla:
    if t % 2 == 0:
        print(t, end=' ')

    
 
    
     