# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 01:00:43 2020

@author: Ana Paula
"""


velocidade = float(input('Digite a velocidade do veículo em Km/h:'))
if velocidade > 80 :
  multa = (velocidade - 80) * 7.0 
  print('Você foi multado no valor de {:.2f}'.format(multa))
else:
    print('Você não ultrapassou a velocidade permitida')
print('Dirija com segurança.')