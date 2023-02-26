# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:54:35 2020

@author: Ana Paula
"""

print('\033[35mJOKENPÔ COM O COMPUTADOR\033[m')
from random import randrange
from time import sleep
print('''Usuário escolha sua jogada:
       [ 1 ] PEDRA
       [ 2 ] PAPEL
       [ 3 ] TESOURA''')
opção = int(input('Qual a jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
computador = randrange(1, 4)
if opção == 1 and computador == 2:
    print('Computador ganhou, pois papel ganha de pedra.!!!', )
elif opção == 1 and computador == 3:
    print('Usuário ganhou, pois pedra ganha de tesoura.')
elif opção == 1 and computador == 1:
    print('Deu empate!')
elif opção == 2 and computador == 1:
    print('Usuário ganhou, pois papel ganha de pedra.')
elif opção == 2 and computador == 3:
    print('Computador ganhou, pois tesoura ganha de papel.')
elif opção == 2 and computador == 2:
    print('Novamente deu empate.')
elif opção == 3 and computador == 1:
    print('Computador ganhou, pois pedra ganha de tesoura.')
elif opção == 3 and computador == 2:
    print('Usuário ganhou, pois tesoura ganha de papel.')
elif opção == 3 and computador == 3:
    print('Deu empate de novo.')
else:
    print('Jogada inválida. Tente Novamente.')
print('-=' * 11)
print('O número escolhido pelo computador foi {}'.format(computador))#

# modo do professor:
#from random import randrange
#itens = ('PEDRA', 'PAPEL', 'TESOURA')    # modo de criar uma 'lista'
#computador = randrange(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))