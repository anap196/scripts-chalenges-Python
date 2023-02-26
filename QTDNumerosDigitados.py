# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:46:08 2020

@author: Ana Paula
"""

número = 0
cont = 0
soma = 0
while número != 999:
  número = int(input('Digite um número: '))
  if número != 999:
     cont += 1
     soma += número 
print('Foram digitados {} números.'.format(cont))
print('A soma entre os números digitados é {}'.format(soma))

# modo do professor:
'''núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))'''
