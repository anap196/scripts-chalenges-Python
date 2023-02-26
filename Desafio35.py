# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:25:28 2020

@author: Ana Paula
"""

n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))
média = (n1 + n2) / 2
if média < 5:
    print('O aluno está REPROVADO!!!')
    print('Sua média foi de {:.2f}'.format(média))
elif média >= 5 and média <= 6.9:
    print('O aluno está de RECUPERAÇÃO!!!')
    print('Sua média foi de {:.2f}'.format(média))
elif média >= 7:
    print('O aluno está APROVADO!!!')
    print('Sua média foi de {:.2f}'.format(média))
print('\033[35mFIM!!!\033[m')