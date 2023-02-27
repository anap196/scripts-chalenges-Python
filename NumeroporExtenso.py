# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:36:48 2020

@author: Ana Paula
"""

contagem = ('Zero', 'Um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
while True:
      número = int(input('Digite um número de 0 a 20: '))
      if 0 <= número <= 20:
         break
print(f'O número escrito por extenso é {contagem[número]}.')

