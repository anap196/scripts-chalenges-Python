# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 00:02:26 2020

@author: Ana Paula
"""

print('*' * 10, 'LOJAS DA ANA BY ANA', '*' * 10)
total = cont = 0
maisbarato = 0
nomebarato = ' '
while True:
    nome = str(input('Qual o nome do produto? ')).strip()
    preço = float(input('Qual o valor do produto? R$ '))
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Usuário deseja continuar? [S/N] ')).strip().upper()[0]
    total += preço
    maisbarato += 1
    if preço >= 1000:
        cont += 1
    if maisbarato == 1:
        maisbarato = preço
        nomebarato = nome
    if preço < maisbarato:
        maisbarato = preço
        nomebarato = nome
    if escolha in 'Nn':
        break
print(f'O total gasto na compra é de R$ {total:.2f}.')
print(f'Temos {cont} produtos que custam mais de R$1000.')
print(f'O produto mais barato na compra feita pelo cliente foi o/a {nomebarato} que custa R${maisbarato:.2f}.')
print('Obrigado pela visita, volte sempre!!!')

# dica do professor:
# podemos simplificar o bloco do segundo if, pois temos uma premissa verdadeira e podemos usar o or;
# if maisbarato == 1 or preço < maisbarato:
#      maisbarato = preço
#      nomebarato = nome