# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:25:08 2021

@author: Ana Paula
"""
aluno = dict()
aluno['nome'] = str(input('Nome do aluno: ')).strip().upper()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >=7.0:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print(f'O nome do aluno é igual a {aluno["nome"]}.')
print(f'A média do aluno é igual a {aluno["média"]}.')
print(f'A situação do aluno(a) {aluno["nome"]} é igual a {aluno["situação"]}.')

#Dica do professor:
# Ao invés de fazer esses prints podemos usar um for;
'''print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} tem valor igual a {v}.')'''
