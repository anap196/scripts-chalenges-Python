# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:52:52 2020

@author: Ana Paula
"""

from random import randrange
computador = randrange(0, 10)
print('Em qual número o computador está pensando? Tente Adivinhar!!!')
print('=' * 40)
jogador = 11
palpite = 0
while jogador != computador:
    jogador = int(input('Digite um número: '))
    palpite += 1
    if jogador == computador:
        print('Parabéns jogador, você adivinhou o número que o computador pensou!!! ')
print('Foram necessários {} palpites para o jogador acertar.'.format(palpite))
print('O computador pensou no número {} e o jogador também pensou no número {}.'.format(computador,jogador))

# modo do professor:
'''from random import randrange
computador = randrange(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou :
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez. ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))'''

    