
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:26:40 2020

@author: Ana Paula
"""

expressão = str(input('Usuário digite uma expressão matemática: '))
parênteses = []
for símb in expressão:
    if símb == '(':
        parênteses.append('(')
    elif símb == ')':
        if len(parênteses) > 0:
            parênteses.pop()
        else:
           parênteses.append(')')
           break
if len(parênteses) == 0:
    print('Sua expressão está válida!!!')
else:
    print('Sua expressão está errada!!!')
