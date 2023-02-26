# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:43:55 2020

@author: Ana Paula
"""


num = int(input('Digite um número de 0 à 9999:'))
print('Unidades de milhar:', num[0:1])
print('Centenas:', num[1:2])
print('Dezenas:', num[2:3])
print('Unidades:', num[3:4])

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

