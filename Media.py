# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:34:00 2020

@author: Ana Paula
"""


aluno = input('Digite o nome do aluno:')
n1    = float(input('Digite a nota:'))
n2    = float(input('Digite a segunda nota:'))
média = ((n1 + n2)/2)
print('A média do aluno {} é {:.1f}'.format(aluno,média))
