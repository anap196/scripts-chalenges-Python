# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 00:52:54 2020

@author: Ana Paula
"""


from random import shuffle
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
sorteado = shuffle(lista)
print('A ordem de apresentação será;{}'.format(lista))

#Explicação do professor, pois não estava conseguindo rodar este programa do
# modo que o professor tinha explicado. 
