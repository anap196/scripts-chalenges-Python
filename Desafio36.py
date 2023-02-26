# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:19:56 2020

@author: Ana Paula
"""
from datetime import date
ano = int(input('Digite o ano de nascimento do atleta:'))
idade = date.today().year - ano 
if idade >= 9 and idade < 14:
    print('A categoria do atleta será a MIRIM.')
elif idade >= 14 and idade < 19:
    print('A categoria do atleta será a INFANTIL.')
elif idade >= 19 and idade < 20:
    print('A categoria do atleta será a JÚNIOR.')
elif idade >= 20:
    print('A categoria do atleta será a SÊNIOR.')
elif idade > 25:
    print('A categoria do atleta será a MASTER.')
print('O atleta tem {} anos'.format(idade))