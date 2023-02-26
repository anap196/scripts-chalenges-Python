# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:04:19 2020

@author: Ana Paula
"""

'''sexo = 'F''M'
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Qual o seu sexo? [F/M] ')).strip().upper()
    print('Digite novamente.')
print('Você é do sexo {}.'.format(sexo))
print('Acabou')'''

# modo do professor:
sexo = str(input('Informe seu sexo: [F/M] ')).strip().upper()[0]  # 0 quer dizer primeira letra.
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))