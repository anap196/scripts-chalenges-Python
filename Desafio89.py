# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:23:52 2021

@author: Ana Paula
"""

dados = {}
pessoas = []
soma = média = 0
while True:
    dados.clear() # apagar os dados antigos para novos dados;
    dados['nome'] = str(input('Qual o seu nome? ')).strip().upper()
    dados['sexo'] = str(input('Qual o seu sexo? [F/M] ')).strip().upper()[0]
    while not dados['sexo'] in 'FfMm':
      dados['sexo'] = str(input('Dados inválidos. Qual o seu sexo? [F/M] ')).strip().upper()[0]    
    dados['idade'] = int(input('Qual a sua idade? '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    opc = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while not opc in 'SsNn':
        opc = str(input('Dados inválidos. Deseja continuar? [S/N] ')).upper()[0]
    if opc in 'Nn':
        break
print('-=' * 30)
'''for c in pessoas:
    totnome += (len(dados) - 2)
print(f'O total de pessoas cadastradas é {totnome}.')'''  # modo Ana de calcular.
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')  #lembrar do comando len!!!
média = soma / len(pessoas)
print(f'A média de idade do grupo é de {média:5.2f} anos.')  # 5 casas ao todo e 2 decimais.
print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():    # prestar atenção na identação Ana Paula!!!
           print(f'{k} = {v}: ', end='')
    print()
print('ENCERRADO!!! VOLTE SEMPRE!!!')
        




    
