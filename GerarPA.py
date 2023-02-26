# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:10:55 2020

@author: Ana Paula
"""


a1 = int(input('Digite o primeiro termo da sua PA: '))
razão = int(input('Digite a razão da sua PA: '))
pa = 0
c = 1
while c < 11:
    pa = a1 + (c - 1) * razão
    print(pa, end=' -> ')
    c += 1
print('\n''Acabou. Temos os 10 primeiros termos da nossa PA.')

# modo do professor:
'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da sua PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')'''
