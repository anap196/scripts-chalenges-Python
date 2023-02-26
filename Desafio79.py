# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:05:08 2020

@author: Ana Paula
"""

result = []
dados = []
quantpess = 0
maior = menor = 0
# Dica do professor: para mostrar a quantidade de pessoas posso usar len(result).
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso Kg: ')))
    if len(result) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    result.append(dados[:])
    dados.clear()
    opção = str(input('Usuário deseja continuar? [S/N] ')).strip()[0]
    while opção not in 'SsNn':
        opção = str(input('Dados inválidos. Usuário deseja continuar? [S/N]')).strip()[0]
    quantpess += 1
    if opção in 'Nn':
        break
#print(f'Nossa lista é: {result}')
print(f'A quantidade de pessoas cadastradas é: {quantpess}')
print(f'O maior peso cadastrado é {maior}Kg. Peso de ', end='')
for p in result:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso cadastrado é {menor}Kg. Peso de ', end='')
for p in result:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()

