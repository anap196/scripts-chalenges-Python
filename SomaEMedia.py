# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:40:51 2020

@author: Ana Paula
"""

num = 0
somanum = 0
médianum = 0
cont = 0
maiorvalor = 0
menorvalor = 0
opção = 'S''N'
while opção != 'N':
   num = int(input('Digite um valor: '))
   somanum += num
   cont += 1
   if cont == 1:
       maiorvalor = menorvalor = num
   else:
         if num > maiorvalor:
            maiorvalor = num
         if num < menorvalor:
             menorvalor = num
   opção = str(input('Usuário deseja continuar? [S/N]' )).upper().strip()
médianum = somanum / cont
print('A média entre os valores digitados é {:.2f}.'.format(médianum))
print('O maior valor lido é {} e o menor valor lido é {}.'.format(maiorvalor, menorvalor))

# modo do professor:
'''resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
média = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, média))
print('O maior valor foi {} e o menor valor é {}.'.format(maior, menor))'''


    
