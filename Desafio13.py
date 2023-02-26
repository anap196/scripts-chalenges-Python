# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:09:56 2020

@author: Ana Paula
"""


funcionário = input('Digite o nome do funcionário:')
salário     = float(input('Digite o valor em reais: R$'))
aumento     = (salário * 0.15)
pagamento   = salário + aumento
print('O novo salário de {} é {:.2f}R$'.format(funcionário, pagamento))
print('O aumento é {:.2f}R$'.format(aumento))

#porcentagem = (15 / 100) * salário
