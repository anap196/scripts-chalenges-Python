# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:02:05 2020

@author: Ana Paula
"""

números = []
par = []
ímpar = []
for c in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        ímpar.append(n)
números.append(par[:])
números.append(ímpar[:])
print(números)
print('*' * 30)
par.sort()
print(f'A lista de valores pares é: {par}')
ímpar.sort()
print(f'A lista de valores ímpares é: {ímpar}')

#Modo do professor:
'''núm = [[],[]]  #criar duas listas vazias dentro de uma lista;
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os números pares digitados foram: {núm[0]}')
print(f'Os números ímpares digitados foram: {núm[1]}')'''
    

    
