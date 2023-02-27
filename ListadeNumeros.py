# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:16:15 2020

@author: Ana Paula
"""

valores = []
maior = menor = 0
for pos in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    if pos == 0:
        maior = valores[pos]
        menor = valores[pos]
    else:
        if valores[pos] > maior:
            maior = valores[pos]
        if valores[pos] < menor:
            menor = valores[pos]
print(f'Guardando os valores em uma lista temos: {valores}')
print(f'O maior valor digitado é: {maior} e encontra-se na posições: ', end='')
for c, v in enumerate(valores):
    if v == maior:
      print(f'{c},', end='')
print()
print(f'O menor valor digitado é: {menor} e encontra-se na posições: ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c},', end='')
print()    # quebra de linha;
