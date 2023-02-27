# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:53:36 2020

@author: Ana Paula
"""

valor = []
while True:
    v = (int(input('Digite um valor: ')))
    if v not in valor:
        valor.append(v)
        print('Valor adicionado na lista!')
    else:
        print('Valor duplicado. Não posso adicionar.')
    resposta = str(input('Usuário deseja continuar? [S/N]')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Tente novamente. Usuário deseja continuar? [S/N] ')).strip()[0]
    if resposta in 'Nn':
        break
valor.sort()
print(f'Guardando em uma lista os valores digitados, temos: {valor}')

