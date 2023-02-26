# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:54:50 2020

@author: Ana Paula
"""


cidade = str(input('Digite o nome de sua cidade:')).strip()
print('santo' in cidade[0:5])
print(cidade[:5].upper() == 'SANTO')


nome = str(input('Digite seu nome completo:')).strip()
print('silva' in nome.lower())