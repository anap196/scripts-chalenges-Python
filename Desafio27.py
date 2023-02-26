# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:47:26 2020

@author: Ana Paula
"""
from datetime import date  #biblioteca que me retorna data
ano = int(input('Digite o ano escolhido:'))
if ano == 0:
    ano = date.today().year   # comando que pega o ano atual configurado no meu computador.
if ano % 4 == 0:
    print('O ano {} escolhido é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
if ano % 100 != 0:
    print('O ano {} escolhido é bissexto'.format(ano))
else:
    print('O ano {} escolhido é bissexto'.format(ano))
if ano % 400 == 0:
      print('O ano {} escolhido é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
    
