# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:15:53 2020

@author: Ana Paula
"""
import math
from datetime import date
ano = int(input('Digite o ano de nascimento da pessoa:'))
diferença = date.today().year - ano
tempo = math.fabs(18 - diferença)
if diferença < 18 and tempo:
    print('O jovem ainda vai se alistar!!!')
    print('Falta {} anos para o jovem se alistar'.format(tempo))
elif diferença == 18:
    print('Chegou a hora do jovem se alistar!!!')
elif diferença > 18 and tempo:
    print('Infelizmente já passou da hora do jovem se alistar!')
    print('Passou {} anos para o alistamento.'.format(tempo))
print('A idade do jovem é de {} anos.'.format(diferença))

