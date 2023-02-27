# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:20:46 2020

@author: Ana Paula
"""

print('#' * 10, 'Banco da ANA', '#' * 10)
tot = diferença = 0
valor = 0
resto = resto1 = resto2 = resto3 = 0
while True:
    saque = int(input('Qual valor deseja sacar? R$ '))
    valor = saque % 50
    if valor != 0:
        tot = saque // 50
        resto = saque - ( tot * 50)
        resto1 = resto // 20
        resto2 = resto - (resto1 * 20)
        resto2 = resto2 // 10
        diferença = resto % 10
        resto3 = diferença // 1
    else:
        if valor == 0:
           tot = saque // 50
    if resto3 == 0 :
        break
print(f'Serão entregues {tot} cédulas de R$ 50 reais.')
print(f'Serão entregues {resto1} cédulas de R$ 20 reais.')
print(f'Serão entregues {resto2} cédulas de R$ 10 reais.')
print(f'Serão entregues {resto3} cédulas de R$ 1 real.')

# modo do professor:
'''print('{}:^30'.format('Banco CEV'))
print('*' * 30)
valor = int(input('Qual valor deseja sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('*' * 30)
print('Tenha um bom dia !')'''



