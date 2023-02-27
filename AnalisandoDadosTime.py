# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 00:58:49 2021

@author: Ana Paula
"""

jogador = {}
total = []
time = list()
while True:
  jogador.clear()
  jogador['nome'] = str(input('Qual o nome do jogador? ')).upper().strip()
  jogador['partidas'] = int(input('Quantas partidas o jogador jogou? '))
  total.clear()
  for c in range(0, jogador['partidas']):
    total.append(int(input(f'Quantos gols o jogador fez na partida {c}? ')))
  jogador['gols'] = total[:]    # colocando minha lista dentro do dicionário;
  jogador['total'] = sum(total)
  time.append(jogador.copy())
  opc = str(input('Deseja continuar? [S/N] ')).upper()[0]
  while opc not in 'SsNn':
      opc = str(input('Dados Inválidos. Por Favor digite novamente. [S/N] ')).upper()[0]
  if opc in 'Nn':
      break
print('*' * 40)
print('cod', end=' ')       # criando um cabeçalho para dar nome as coisas;
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k , v in enumerate(time):       # criando uma tabela para apresentar os dados;
    print(f'{k:>3} ', end='')     
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('*' * 40)
print('ANALISANDO OS JOGADORES...')
while True:
    busca = int(input('Deseja ver os dados de qual jogador? (999 para parar o programa!!!)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!!! Não existe jogador com o código {busca}.')
    else:
        print(f'---LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):    # buscando dentro da lista time o código e a quantidade de gols.
            print(f'   No jogo {i} fez {g} gols.')
        print('*' * 40)
print('VOLTE SEMPRE!!!')
        
    
    
