# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:04:40 2020

@author: Ana Paula
"""

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc >=18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade')
elif imc >= 40:
    print('Você está com obesidade mórbida.')
print('O valor do imc é {:.2f}'.format(imc))