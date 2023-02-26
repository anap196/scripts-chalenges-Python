# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:46:04 2020

@author: Ana Paula
"""

from time import sleep
matriz = []
linha1 = []
linha2 = []
linha3 = []
for l in range(0, 3):
    n1 = int(input('Digite um valor: '))
    linha1.append(n1)
for l in range(0, 3):
        n2 = int(input('Digite um valor: '))
        linha2.append(n2)
for l in range(0, 3):
        n3 = int(input('Digite um valor: '))
        linha3.append(n3)
matriz.append(linha1)
matriz.append(linha2)
matriz.append(linha3)
print('MONTANDO NOSSA MATRIZ...')
sleep(1)
print('*' * 30)
print(matriz[0][0],'|', matriz[0][1],'|', matriz[0][2])
print(matriz[1][0],'|', matriz[1][1],'|', matriz[1][2])
print(matriz[2][0],'|', matriz[2][1],'|', matriz[2][2])

#Modo do professor:
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
       print(f'[{matriz[l][c]:^5}]' , end='')
    print()'''
