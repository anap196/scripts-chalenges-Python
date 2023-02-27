# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:42:45 2020

@author: Ana Paula
"""
#dados =  []
resultado = []
while True:
    nome = str(input('Qual o nome do aluno: ')).strip().upper()
    n1 = float(input('Qual a primeira nota do aluno? '))
    n2 = float(input('Qual a segunda nota do aluno?  '))
    média = (n1 + n2)/2
    resultado.append([nome, [n1, n2], média])
    opção = str(input('Deseja continuar? [S/N] ')).strip()[0]
    while opção not in 'NnSs':
      opção = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if opção in 'Nn':
        break
print('*' * 30)
print(' BOLETIM DOS ALUNOS ')
print('*' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
#print(resultado)
#print(n[0])
for i, r in enumerate(resultado):
  print(f'{i:<4}{r[0]:<10}{r[2]:>8.1f}')      # alinhando à direita para ficar em forma de tabela.
while True:
   pergunta = int(input('Deseja ver as notas de qual aluno? (999 para interromper): '))
   if pergunta == 999:
       print('FINALIZANDO...')
       break
   if pergunta <= len(resultado) - 1:
       print(f'Notas de {resultado[pergunta][0]} são {resultado[pergunta][1]}')
print('VOLTE SEMPRE!!!')
# precisei de algumas dicas do professor para terminar de fazer, pois a segunda parte eu 
# não dei conta de fazer. Interessante as partes do print.

    
