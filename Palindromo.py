# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:44:24 2020

@author: Ana Paula
"""
        
# modo do professor porque eu não dei conta :
frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()     # separar a frase em palavras dentro de uma lista;
junto = ''.join(palavras)    # juntar as palavras que estão separadas sem espaços;
inverso = junto[::-1]        # lendo a string de trás para frente sem saber início e fim;
print('O inverso de {} é {}'.format(junto, inverso))
'''for letra in range(len(junto) - 1, -1, -1):    # ler o tamanho da string de trás para frente;
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))'''
if inverso == junto:
    print('Temos um PALÍNDROMO.')
else:
    print('Não temos um PALÍNDROMO.')



