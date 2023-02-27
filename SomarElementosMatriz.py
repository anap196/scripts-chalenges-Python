# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:56:37 2020

@author: Ana Paula
"""

matriz = []
linha1 = []
linha2 = []
linha3 = []
somapar = 0
for l in range(0, 3):
    l1 = int(input('Digite um valor para 1ª linha: '))
    linha1.append(l1)
    if l1 % 2 == 0:
        somapar += l1
for l in range(0, 3):
    l2 = int(input('Digite um valor para 2ª linha: '))
    linha2.append(l2)
    if l2 % 2 == 0:
       somapar += l2
for l in range(0, 3):
    l3 = int(input('Digite um valor para 3ª linha: '))
    linha3.append(l3)
    if l3 % 2 == 0:
        somapar += l3
matriz.append(linha1)
matriz.append(linha2)
matriz.append(linha3)
print('MONTANDO A MATRIZ...')
print(matriz[0][0],'|', matriz[0][1],'|', matriz[0][2])
print(matriz[1][0],'|', matriz[1][1],'|', matriz[1][2])
print(matriz[2][0],'|', matriz[2][1],'|', matriz[2][2])
print('-=' * 20)
print('ANALISANDO NOSSA MATRIZ TEMOS...')
print('-=' * 20)
print(f'A soma de todos os valores pares digitados é: {somapar}')
terceira = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é: {terceira}')
if matriz[1][0] > matriz[1][1]:
    maior = matriz[1][0]
else: 
    if matriz[1][0] > matriz[1][2]:
       maior = matriz[1][0]
if matriz[1][1] > matriz[1][0]:
       maior = matriz[1][1]
else:
    if matriz[1][1] > matriz[1][2]:
       maior = matriz[1][1]
if matriz[1][2] > matriz[1][0]:
       maior = matriz[1][2]
else:
    if matriz[1][2] > matriz[1][1]:
       maior = matriz[1][2]
print(f'O maior valor da segunda linha é: {maior}')

#Modo do professor:
# usar exercício anterior para montar a matriz...
# spar = scol = mai = 0 ---- iniciando as variáveis;
# no momento que for exibir a matriz na tela  eu faço o seguinte:
# if matriz[l][c] % 2 == 0:
#   spar += matriz[l][c]
# print()
#print('-=' * 30)
#print(f'A soma de todos os valores pares são: {spar}')
# for l in range(0, 3):
#     scol += matriz[l][2]
# print(f'A soma dos valores da 2ª coluna são: {scol})
# for c in range(0, 3):
#     if c == 0:
#        mai = matriz[1][c]
#     elif matriz[1][c] > mai:
#        mai = matriz[1][c]
# print(f'O maior valor da 2ª linha é: {mai})
