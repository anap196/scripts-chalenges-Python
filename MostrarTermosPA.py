# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 18:25:13 2020

@author: Ana Paula
"""

# não dei conta de fazer;
# resolução toda do professor;
print('Gerador de PA')
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
      print('{} -> '.format(termo), end='')
      termo += razão
      cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

         


    
