# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:38:06 2021

@author: Ana Paula
"""
from datetime import date
dados = dict()
dados['nome'] = str(input('Qual o seu nome? ')).strip().upper()
nascimento    = int(input('Qual o seu ano de nascimento? '))
dados['idade'] = date.today().year - nascimento
dados['ctps'] = int(input('Qual o número da sua carteira de trabalho? 0 caso não tenha! '))
if dados['ctps'] != 0:
        dados['contratação'] = int(input('Qual ano o funcionário foi contratado? '))
        dados['salário'] =  float(input('Qual o valor do salário? R$ '))
        dados['aposentadoria'] = (dados['contratação'] - nascimento + 35)
for k, v in dados.items():
    print(f'{k} tem valor igual a {v}.')
    


