# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 14:44:27 2020

@author: Ana Paula
"""

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
if n1 > n2:
    print('O maior valor é {} e o menor valor é {}'.format(n1, n2))
elif n2 > n1:
    print('O maior valor é {} e o menor valor é {}'.format(n2, n1))
elif n1 == n2:
    print('Não existe maior, pois os dois números são iguais.')
#elif n2 == n1:
#    print('Não existe maior, pois os dois números são iguais.')
print('Comparação entre dois números!!!')

# como não existe uma quarta opção eu poderia usar o else para comparar n1 == n2;