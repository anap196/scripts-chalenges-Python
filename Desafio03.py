# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:25:22 2020

@author: Ana Paula
"""

primeiro = int(input('Qual o primeiro número?'))
segundo  = int(input('Qual o segundo número?'))
soma     = primeiro  + segundo
#print(' A soma entre 2 e 7 é' , soma) = formato antigo no phyton
print('A soma entre {} e {} é {}' .format(primeiro, segundo, soma))


