# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:26:00 2020

@author: Ana Paula
"""

import math
r1 = float(input('Digite o primeiro comprimento:'))
r2 = float(input('Digite o segundo comprimento:'))
r3 = float(input('Digite o terceiro comprimento:'))
if math.fabs(r2 - r3) < r1 < (r2 + r3): 
 if math.fabs(r1 - r3) < r2 < (r1 + r3):
   if math.fabs(r1 - r2) < r3 < (r1 + r2):
       print('Respeitada todas as condições teremos um triângulo. EBA!!!')
else:
    print('Não podemos ter um triângulo')
print('--FIM--')


# Jeito do professor:
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
# print('Os segmentos acima podem formar um triângulo)
#else:
#  print('Os segmentos acima não podem formar um triângulo.)  
  
    
