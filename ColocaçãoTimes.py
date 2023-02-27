# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:51:54 2020

@author: Ana Paula
"""

times = (' INTERNACIONAL', ' VASCO', ' ATLÉTICO-MG', ' PALMEIRAS', ' SÃO PAULO', ' SANTOS',
         ' FLUMINENSE', ' BAHIA', ' GRÊMIO', ' ATLÉTICO-PR', ' BOTAFOGO', ' BRAGANTINO',
         ' FLAMENGO', ' CORINTHIANS', ' GOIÁS', ' FORTALEZA', ' ATLÉTICO-GO',
         ' SPORT', ' CEARÁ-SC', ' CORITIBA')
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print(f'Os últimos quatro colocados são: {times[16:20]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('Nesse caso não tenho chapecoense, pois ela está na série B.')
for pos, times in enumerate(times):
    print(f'O time {times} está na posição {pos}.')


#for t in times:
#    print(t)   # maneira de deixar organizado.
# modo do professor:
#print(f'Os quatro últimos colocados são: {times[-4:]}')
