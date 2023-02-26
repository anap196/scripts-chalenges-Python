# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:19:57 2020

@author: Ana Paula
"""


pessoa = input('Digite o nome da pessoa:')
dinheiro = float(input('Digite a quantidade existente na carteira: R$'))
doláres = (dinheiro / 3.27) 
print('A quantidade de doláres que {} pode comprar é {:.2f}US$'.format(pessoa,doláres))