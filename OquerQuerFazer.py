# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:11:21 2020

@author: Ana Paula
"""


soma = 0
menu = 0
n1 = int(input('Qual o primeiro valor? '))
n2 = int(input('Qual o segundo valor? '))
while menu != 5: 
   print('''Nosso MENU:
      [1] SOMAR
      [2] MULTIPLICAR
      [3] MAIOR
      [4] NOVOS NÚMEROS
      [5] SAIR DO PROGRAMA''')
   menu = int(input('Usuário escolha sua opção: '))
   soma = n1 + n2
   multiplicação = n1 * n2
   maior = n1
   if menu == 1:
       print('A soma entre os numeros é igual à {}.'.format(soma))
   elif menu == 2:
       print('A multiplicação entre os números é {}.'.format(multiplicação))
   elif menu == 3 and n2 < n1:
       print('O maior valor é {}.'.format(maior))
   elif menu == 3 and n2 > n1:
       print('O maior valor é {}.'.format(n2))
   elif menu == 4:
       print('Novos valores: ')
       n1 = int(input('Digite um novo valor: '))
       n2 = int(input('Digite um novo valor: '))
   elif menu == 5:
       print('Fim do programa...')
   else:
       print('Opção inválida.')
    

# modo do professor:
#from time import sleep
#n1 = int(input('Primeiro valor: '))
#n2 = int(input('Segundo valor: '))
#opção = 0
#while opção != 5:
#    print(''' Nosso MENU:
#          [ 1 ] SOMAR
#          [ 2 ] MULTIPLICAR
#          [ 3 ] MAIOR
#          [ 4 ] NOVOS NÚMEROS
#          [ 5 ] SAIR DO PROGRAMA''')
#    opção = int(input('Qual a sua opção? '))
#    if opção == 1:
#        soma = n1 + n2
#        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
#    elif opção == 2:
#        produto = n1 * n2
#        print('O resultado entre {} x {} é {}.'.format(n1, n2, produto))
#    elif opção == 3:
#        if n1 > n2:
#            maior = n1
#       else:
#            maior = n2
#        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
#    elif opção == 4:
#        print('Informe os números novamente ')
#        n1 = int(input('Primeiro valor: '))
#        n2 = int(input('Segundo valor: '))
#    elif opção == 5:
#        print('Finalizando...')
#    else:
#        print('Opção inválida. Tente novamente.')
#    print('=-=' * 10)
#    sleep(1)
#print('Fim do programa. Volte sempre!')'''
