# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:36:44 2020

@author: Ana Paula
"""


produtos = ('Leite', ' 3.50', 'Café',' 9.98', 'Pão', ' 2.00','Pão de queijo', ' 12.00', 'Presunto', ' 15.50',
            'Muçarela', ' 20.75', 'Filtro de Papel', ' 3.75', 'Açucar',  ' 8.78', 'Macarrão', ' 3.99',
            'Extrato de Tomate', ' 4.49', 'Arroz', ' 15.48', 'Feijão', ' 8.99')
print('*' * 30)
print('TABELA DE PREÇOS E PRODUTOS')
print('*' * 30)
for cont in range(0, len(produtos)):
    if cont % 2 == 0:
       print(f'{produtos[cont]:=<20}', end='')
    else:
        print(f'R${produtos[cont]:>7}')
print('*' * 30)
