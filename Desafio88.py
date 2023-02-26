# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 19:36:18 2021

@author: Ana Paula
"""

print('*' * 50)
print('GERENCIAMENTO DE UM JOGADOR DE FUTEBOL')
print('*' * 50)
totgols = 0
jogador = dict()
resultado = list()
jogador['nome'] = str(input('Qual o nome do jogador? ')).strip().upper()
jogador['partidas'] = int(input('Quantas partidas o jogador jogou? '))
for c in range(0, jogador['partidas']):
    resultado.append(int(input(f'Quantos gols o jogador fez na partida {c}? ')))
jogador['gols'] = resultado[:]    # colocando minha lista dentro do dicionário;
for c in resultado:
    totgols += c
jogador['total'] = totgols
#outra maneira de somar o total de gols feito pelo jogador é:
# jogador['total'] = sum(resultado); ou seja, temos uma função para somar;
print('*' * 40)
print('Mostrar de 3 formas diferentes...')
print()
print(jogador)
print('*' * 40)
for k, v in jogador.items():
    print(f'{k} tem valor {v}.')
print('*' * 40)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
#print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.') Modo do professor.
for i, v in enumerate(jogador['gols']):
    print(f'   -> Na partida {i}, fez um total de {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

