# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 20:36:57 2020

@author: Ana Paula
"""

s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    par = n % 2
    if par == 0:
       s += n 
       print('A somatória dos números pares será de {}'.format(s))
    elif par != 0:
        print('Opção inválida. Tente novamente.')
print('Fim')

# modo do professor:
'''soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você me informou {} números PARES e a soma foi de {}'.format(cont, soma))'''

        
