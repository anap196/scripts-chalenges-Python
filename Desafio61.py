# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:24:22 2020

@author: Ana Paula
"""

número = 0     # não preciso inicializar a variável número, pois a condição while está verdadeira.
cont = soma = 0
while True:
    número = int(input('Digite um número (999 para parar):'))
    if número == 999:
        break
    cont += 1
    soma += número
print(f'A quantidade de números digitados foi {cont}.')
print(f'A soma dos números digitados equivale a {soma}.')
