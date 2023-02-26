# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:39:11 2020

@author: Ana Paula
"""

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nome = ''
totmulher = 0
for p in range(1, 5):
    nome = str(input('Digite seu nome: ')).strip().upper()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual o seu sexo? [F/M]: ')).strip()  # o in substitui o problema de letra maiusc/minusc.
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {:.2f} anos'.format(médiaidade))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('A quantidade de mulheres que tem menos de 20 anos é {}'.format(totmulher))

# exercício para analisar dados!!!
    
