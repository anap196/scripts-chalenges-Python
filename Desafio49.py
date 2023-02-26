# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:29:14 2020

@author: Ana Paula
"""

# Exercício para analisar dados!!!

from datetime import date
ano = date.today().year 
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nascimento= int(input('Digite seu ano de nascimento: '))
    idade = ano - nascimento
    if idade >= 21:
       totmaior += 1
    elif idade < 21:
        totmenor += 1
print('Ao todo temos {} pessoas maiores de idade.'.format(totmaior))
print('E também temos {} pessoas menores de idade.'.format(totmenor))



# eu complementei meu programa, pois não estava conseguindo ler quantas pessoas eram
# maiores e quantas eram menores.
# muito burra esqueci de criar a variável de contar;
