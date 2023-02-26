# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:09:45 2020

@author: Ana Paula
"""


frase = str(input('Digite uma frase qualquer:')).upper().strip()
print(frase.count('A'))
print(frase.find('A')+1)
print(frase.rfind('A')+1)


nome = str(input('Digite seu nome completo:')).strip().lower()
separa = nome.split()
print('Muito prazer em te conhecer!')
print('O primeiro nome é {}'.format(separa[0]))
print('O último nome é {}'.format(separa[len(separa)-1]))
