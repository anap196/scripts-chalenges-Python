# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:56:58 2020

@author: Ana Paula
"""

from random import randrange
print('Vamos jogar PAR ou ÍMPAR? ')
print('==' * 30)
vitórias = 0
while True:
    jogador = int(input('Qual seu número jogador? '))
    computador = randrange(0, 10)
    soma = (jogador + computador)
    escolha = ' '
    while escolha not in 'PI':
          escolha = str(input('Você quer PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Resultando em {soma}.')
    if escolha == 'P':
        if soma % 2 == 0:
           print('Você ganhou, uhu. Parabéns jogador!!!')
           vitórias += 1
        else:
           print('Você PERDEU!!!')
           break
    if escolha == 'I':
        if soma % 2 == 1:
           print('Você ganhou, uhu. Parabéns jogador!!!')
           vitórias += 1
        else:
          print('Você PERDEU!!!')
          break
print(f'Você conseguiu {vitórias} vitórias consecutivas.')
        

