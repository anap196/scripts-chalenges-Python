# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:16:18 2020

@author: Ana Paula
"""

valor = float(input('Digite o valor do imóvel:R$'))
salário = float(input('Digite o valor do salário: R$'))
tempo = int(input('Quantos anos o cliente quer pagar:'))
ano = tempo * 12
prestação = valor / ano
if prestação == valor / ano and prestação <= 0.3 * salário:
    print('O valor da prestação mensal será de {:.2f}'.format(prestação))
    print('Cliente consegue o empréstimo.')
else:
    print('Infelizmente o empréstimo foi negado.')
    print('O valor da prestação seria de {:.2f}'.format(prestação))
print('\033[36m' 'Simulação para comprar um imóvel!!!\033[m')
    

#modo do professor:
#mínimo = salário * 30 / 100
#if prestação <= mínimo:
#    print('Cliente consegue o empréstimo.)
