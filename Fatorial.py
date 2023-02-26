# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:46:16 2020

@author: Ana Paula
"""

'''from math import factorial
num = 1
while num != 0:
    num = int(input('Digite um número: '))
    print('O fatorial de {} é {}.'.format(num, factorial(num)))
print('Acabou')

# modo do professor:
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1        # para a multiplicação ficar 'limpa'= dá o mesmo valor
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

# Desafio do professor:
# refazer o programa usando o for;
n = int(input('Digite o número para saber o fatorial: '))
f = 1
for c in range(n, 0, -1):
    print(c, end='')
    print('x' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))
    
