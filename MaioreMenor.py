# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 22:10:53 2020

@author: Ana Paula
"""


n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
n3 = float(input('Digite mais um número:'))
# Verificando o menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando o maior valor:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor entre os números digitados é {}'.format(menor))
print('O maior entre os números digitados é {}'.format(maior))

# Este método foi o professor quem ensinou, pois eu usei uma forma diferente que
# deu errado. Chama de método de testagem, o qual considera um valor fixo e testa
# todos os outros.
 

    
    
