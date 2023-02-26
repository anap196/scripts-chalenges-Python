# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:17:09 2020

@author: Ana Paula
"""
num = int(input('Digite um número:'))
Usuário = int(input('Usuário escolha qual será a base entre 1, 2 ou 3 de conversão:')) 
binário = bin(num)
octal = oct(num)
hexadecimal = hex(num)
1 == binário
2 == octal
3 == hexadecimal
if Usuário == int(1):
   print('O número {} convertido em binário é {}'.format(num, binário))
elif Usuário == int(2):
   print('O número {} convertido em octal é {}'.format(num, octal))
elif Usuário == int(3):
   print('O número {} convertido em hexadecimal é {}'.format(num, hexadecimal))
   
   #modo do professor:
#num = int(input('Digite um número:'))
#print('''Escolha uma das bases para conversão:
#[ 1 ] converter para BINÁRIO
#[ 2 ] converter para OCTAL
#[ 3 ] converter para HEXADECIMAL''') #três aspas servem para poder conseguir fazer várias linhas.
#opção = int(input('Digite sua opção:'))
#if opção == 1:
#    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
#elif opção == 2:
#    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
#elif opção == 3:
#    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')

