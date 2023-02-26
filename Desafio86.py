# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:01:20 2021

@author: Ana Paula
"""

from random import randrange
from time import sleep
from operator import itemgetter    # elemento para colocar dicionário em ordem;
#maior = menor = 0
dados = {'jogador1': randrange(1, 6), 'jogador2': randrange(1, 6),
         'jogador3': randrange(1, 6), 'jogador4': randrange(1, 6)}
'''print('-=' * 30)
print(f'O 1º jogador tirou o número {dados["jogador1"]}.')
print(f'O 2º jogador tirou o número {dados["jogador2"]}.')
print(f'O 3º jogador tirou o número {dados["jogador3"]}.')
print(f'O 4º jogador tirou o número {dados["jogador4"]}.')
print('-=' * 30)
for j in dados.values():
    if j == 0:
        j = maior
    else:
        if j > maior:
            maior = j
print(f'O vencedor foi quem tirou o número {maior}.')'''
ranking = {}  # criando um novo dicionário para colocar em ordem;
print('VALORES SORTEADOS:')
for k, v in dados.items():
    print(f'{k} tirou valor igual a {v} no dado.')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)