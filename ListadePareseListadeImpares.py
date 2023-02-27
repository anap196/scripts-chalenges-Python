# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:31:30 2020

@author: Ana Paula
"""

lista = list()
par = []
ímpar = []
while True:
    lista.append(int(input('Digite um número: ')))
    escolha = str(input('Usuário deseja continuar? [S/N] ')).strip()[0]
    while escolha not in 'SsNn':
        escolha = str(input('Dados inválidos. Usuário quer continuar? [S/N]')).strip()[0]
    if escolha in 'Nn':
        break
print(f'Nossa lista completa é: {lista}')
for l in lista:
   if l % 2 == 0:
       par.append(l)
   else:
       if l % 2 == 1:
         ímpar.append(l)
print(f'A lista de números pares é: {par}')
print(f'A lista de números ímpares é: {ímpar}')

# modo do professor:
'''num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'Nossa lista completa é: {num}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {ímpares}')'''
