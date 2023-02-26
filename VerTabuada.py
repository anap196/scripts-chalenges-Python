# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:05:42 2020

@author: Ana Paula
"""

print('-=' * 20)
while True:
    num = int(input('Digite um valor para ver sua tabuada: '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
     print(f'{num} x {c} = {num * c}')
    print('-' * 30)
print('Acabou!!!')

# estava colocando o break no lugar errado, por isso não conseguia parar o programa.
    
       
     

