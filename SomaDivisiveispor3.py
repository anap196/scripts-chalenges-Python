# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:29:46 2020

@author: Ana Paula
"""

'''s = 0    # acumulador 
for c in range(1, 500+1):
    resto = c % 2      # números ímpares com resto diferente de 0;
    ímpares = c % 3    # números ímpares que são múltiplos de 3 ou seja, resto zero.
    if resto != 0 and ímpares == 0:
      s += c  
      print(s)
print('A somatória de todos os números ímpares e divisíveis por 3 é {}'.format(s))'''


#modo do professor:
soma = 0
cont = 0      # contador = sempre soma mais 1.
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
    
    
     
    
     
    
