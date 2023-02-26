# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:12:05 2020

@author: Ana Paula
"""


from math import sqrt, pow
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
h = sqrt(pow(co,2) + pow(ca, 2))
print('O valor da hipotenusa é {:.2f}'.format(h))

#Explicação do professor:

'''from math import hypot
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hi = hypot(co, ca)
print('O valor da hipotenusa será de {:.2f}'.format(hi))'''

#Outro método seria: hi = (co ** 2 + ca ** 2) ** (1/2)
