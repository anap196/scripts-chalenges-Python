# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:58:11 2020

@author: Ana Paula
"""

print('-*' * 30)
print('{:^60}'.format('MEGA SENA'))
print('-*' * 30)
from random import randrange
from time import sleep
palpites = []
jogos = []
jogador = int(input('Quantos jogos o jogador quer? '))
print('SORTEANDO OS NÚMEROS...')
sleep(1)
tot = 1
while tot <= jogador:
    cont = 0
    while True:
      números = randrange(1, 60)
      if números not in palpites:
       palpites.append(números)
       cont += 1
      if cont >= 6:
         break
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()
    tot += 1
#print(f'Os jogos sorteados pela máquina são: {jogos}')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
print('BOA SORTE!!!')



