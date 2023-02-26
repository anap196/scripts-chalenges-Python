# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:18:06 2020

@author: Ana Paula
"""


from math import cos, sin, tan, radians
ang = float(input('Digite um valor em graus:'))
c   = cos(radians(ang))
s   = sin(radians(ang))
t   = tan(radians(ang))
print('O cosseno do ângulo {} é {:.2f}, o seno é {:.2f} e a tangente é {:.2f}'.format(ang, c, s, t))

#esqueci de converter as unidades, por isso o cálculo estava errado.
