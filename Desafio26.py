# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:09:07 2020

@author: Ana Paula
"""


distância = float(input('Digite a distância da viagem em Km:'))
if distância <= 200:
    passagem = 0.50 * distância
    print('O preço da passagem é de {:.2f}'.format(passagem))
else:
    passagem = 0.45 * distância
    print('O preço da passagem é de {:.2f}'.format(passagem))
print('Tenha uma boa viagem!!!')



# outro modo de fazer que o professor ensinou:
# preço = distância * 0.50 if distância <= 200 else distância * 0.45