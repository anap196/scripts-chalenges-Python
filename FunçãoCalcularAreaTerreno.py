# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:22:04 2021

@author: Ana Paula
"""
def área(l, c):
    área = (largura * comprimento) / 2
    print(f'A área do terreno é igual a {área:.2f}m².')
largura     = float(input('Qual a largura do terreno m? '))
comprimento = float(input('Qual o comprimento do terreno m? '))
área(largura, comprimento)
