# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:15:32 2020

@author: Ana Paula
"""

palavras = ('ana', 'gustavo', 'aprender', 'programar', 'hacker', 'trabalho', 'futuro',
            'carreira', 'objetivos', 'vida', 'sonhos', 'familia', 'dinheiro', 'carro',
            'curso', 'faculdade', 'amigos', 'sorte', 'comida', 'dormir')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
# for vai analisar cada elemento da lista/ tupla.
