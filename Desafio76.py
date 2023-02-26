# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 14:23:04 2020

@author: Ana Paula
"""

números = []
quant = 0
resposta=''
while True:
    números.append(int(input('Digite um número: ')))
    números.sort(reverse=True)
    resposta = str(input('Usuário deseja continuar? [S/N] ')).strip()[0]
    while resposta not in 'SsNn':
       resposta = str(input('Dados inválidos, tente novamente. Usuário deseja continuar? [S/N] ')).strip()[0]
    quant += 1
    if resposta in 'Nn':
        break
print(f'A lista ordenada decrescente é: {números}')
print(f'O usuário digitou {quant} números.')
if 5 in números:
    print('O número 5 foi digitado e adicionado na lista.')
else:
    print('O número 5 não foi digitado e não está na lista.')
    
# modo do professor:
'''valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('*' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')'''