# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:41:33 2020

@author: Ana Paula
"""


nome = str(input('Digite seu nome completo:')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


#não consegui fazer o programa todo, então as últimas partes são resoluções do
#professor. Não raciocinei que podia contar espaços.


