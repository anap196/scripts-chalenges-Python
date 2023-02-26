# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:43:29 2020

@author: Ana Paula
"""

r1 = float(input('Digite o comprimento:'))
r2 = float(input('Digite o segundo comprimento:'))
r3 = float(input('Digite o terceiro comprimento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Conseguimos formar um triângulo' , end='') #end = colocar a palavra equilatero do lado
#x = r1
#if r2 == x and r3 != x:         #outra maneira de aninhar if dentro do if;
#    print('Teremos um triângulo isósceles.')
#elif r2 != x and r3 == x:
#    print('Teremos um triângulo isósceles.')
#elif r2 != x and r3 != x:
#    print('Teremos um triângulo escaleno.')
#elif r2 == x and r3 == x:
#    print('Teremos um triângulo equilátero.')
    
#modo do professor:
    if r1 == r2 == r3:
     print('EQUILÁTERO!')
    elif r1 != r2 != r3 !=r1:
     print('ESCALENO')
    else:
      print('ISÓSCELES')
else:
    print('Não podemos formar um triângulo.')
    