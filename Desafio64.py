# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 23:15:36 2020

@author: Ana Paula
"""

print('==' * 10, 'CADASTRAMENTO DE PESSOAS', '==' * 10)
cont = quantidade = quant = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo? [F/M] ')).strip().upper()[0]
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Usuário deseja continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        cont += 1
    if sexo in 'Mm':
        quantidade += 1
    if sexo in 'Ff' and idade < 20:
        quant += 1
    if escolha in 'Nn':
        break
print(f'Ao todo temos {cont} pessoas com mais de 18 anos cadastradas.')
print(f'Temos {quantidade} homens cadastrados.')
print(f'Ao todo temos {quant} mulheres com menos de 20 anos cadastradas.')