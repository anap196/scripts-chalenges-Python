# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:15:44 2020

@author: Ana Paula
"""


salário = float(input('Digite o valor do salário em R$:'))
if salário > 1250:
    aumento = (salário * 10/100) + salário
    print('O funcionário irá receber um valor de {:.2f}R$'.format(aumento))
else:
    aumento = (salário * 15/100) + salário
    print('O funcionário irá receber um valor de {:.2f}R$'.format(aumento))