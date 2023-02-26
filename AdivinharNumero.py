# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:09:55 2020

@author: Ana Paula
"""


import random
from time import sleep  #biblioteca que faz o pc "dormir" por alguns segundos
npc = random.randrange(0, 5)  #Faz o computador "pensar"
n = int(input('Jogador digite um número de 0 a 5:')) #jogador tenta adivinhar o número
print('PROCESSANDO...')
sleep(3)
if n == npc:
    print('Jogador ganhou. Parabéns!!!')
else:
    print('Jogador perdeu. Tente mais uma vez!!!')
print('O número escolhido pelo computador foi {}'.format(npc))
print('--FIM--')
print('==' * 20)
