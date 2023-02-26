# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:54:09 2020

@author: Ana Paula
"""


# Exercício para analisar dados!!!
pesomaior = 0
pesomenor = 0
for p in range(1, 6):    
    peso = float(input('Digite seu peso:Kg '))
    if p == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('O maior peso lido foi de {} Kg'.format(pesomaior))
print('E o menor peso lido foi de {} Kg.'.format(pesomenor))