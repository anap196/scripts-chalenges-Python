# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:53:55 2020

@author: Ana Paula
"""

print('{:=^40}'.format('LOJAS DA ANA'))
preço = float(input('Digite o valor do produto.R$'))
print('''Escolha qual será o modo de pagamento:
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista no cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
opção = int(input('Cliente escolhe a opção de pagamento:'))
avista = preço - (preço * 10 / 100)
cartão = preço - (preço * 5 / 100)
cartão2x = preço 
cartão3x = preço + (preço * 20 / 100)
if opção == 1:
    print('O cliente ganhará desconto e pagará um valor de {:.2f}R$'.format(avista))
elif opção == 2:
    print('O cliente ganhará um desconto e pagará um valor de {:.2f}R$'.format(cartão))
elif opção == 3:
         parcela = preço / 2
         print('Sua compra será parcelada em 2x de {:.2f}R$'.format(parcela))
         print('O cliente não ganhará desconto então o preço será de {:.2f}R$.'.format(preço))
elif opção == 4:
    totparc = int(input('Em quantas vezes o cliente gostaria de parcelar?'))
    parcela = preço / totparc
    print('Sua compra será parcelada em {}x de {:.2f}R$'.format(totparc, parcela))
    print('O cliente terá um acréscimo de juros e pagará um valor de {:.2f}R$'.format(cartão3x))
else:
    total = preço
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE!')  #evitar que dê problema se o cliente digitar opção errada
   
         
    


    
