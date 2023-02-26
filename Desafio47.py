# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:05:41 2020

@author: Ana Paula
"""

'''for c in range(2, 50):
    par = c % 2
    pri = c % 3
    primo = c % 5
    p = c % 7
    if par == 0 and c != 2:
        print('O número {} não é primo.'.format(c))
    elif pri == 0 and c != 3:
        print('O número {} não é primo.'.format(c))
    elif primo == 0 and c != 5:
        print('O número {} não é primo.'.format(c))
    elif p == 0 and c != 7:
        print('O número {} não é primo.'.format(c))
    elif par != 0 or pri != 0 or primo != 0 or p != 0:
        print('O número {} é primo.'.format(c))
print('Fim')'''

# modo do professor:
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print(end=' ')
        tot += 1
    else:
        print(end=' ')
    print('{}'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO.')
else:
    print('E por isso ele não é PRIMO.')


