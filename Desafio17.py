# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:43:57 2020

@author: Ana Paula
"""

import random
sorteado = random.choice(['Ana', 'Gustavo', 'Isabela', 'Justin'])
print('O sorteado foi {}'.format(sorteado))


import random
ordem = random.sample(['Ana', 'Gustavo', 'Isabela', 'Justin'], k=4)
print('A ordem de apresentação será {}'.format(ordem))


#Explicação do professor:
'''from random import choice
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno sorteado foi {}'.format(escolhido))'''

                                                

         