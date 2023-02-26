# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:31:09 2020

@author: Ana Paula
"""

número = []
maior = menor = 0
for cont in range(0, 5):
    n = (int(input('Digite um número: ')))
    if cont == 0 or n > número[-1]:
        número.append(n)
    else:
        pos = 0
        while pos < len(número):
            if n <= número[pos]:
                número.insert(pos, n)
                break
            pos += 1
print(f'Guardando os valores ordenados em uma lista temos: {número}')


