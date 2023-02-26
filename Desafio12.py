# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:56:31 2020

@author: Ana Paula
"""


produto = input('Digite o nome do produto:')
preço   = float(input('Digite o valor do produto: R$'))
desconto = (0.05 * preço)
valor    = preço - desconto
print('O novo preço do {} é {:.2f}R$'.format(produto,valor))
print('Valor do desconto é {:.2f}R$'.format(desconto))

