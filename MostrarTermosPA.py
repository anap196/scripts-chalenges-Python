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

         

# Refazendo o exercício depois para estudar e aprender
  # -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:21:19 2020
@author: Ana Paula
"""

a1 = int(input('Primeiro termo da sua PA: '))
razão = int(input('Razão da sua PA: '))
cont = 1
termo = a1
opção = 10     # quantidade inicial de termos que eu já tenho;
total = 0
while opção != 0:
    total = total + opção
    while cont < total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('==' * 20)
    opção = int(input('Usuário quer mostrar mais quantos termos? '))
print('Acabou.')  
