# -*- coding: utf-8 -*-
"""Cara-Coroa

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XImAWa6eWYFGUtZYC49hCnTGMCJRhPB1
"""

import random

user_input = int(input('Insira o número de jogadas: '))
lados_moeda = ['cara','coroa'] 
cara_coroa = [] 
for i in range(user_input):
    jogadas = random.choice(lados_moeda)
    cara_coroa.append(jogadas)
print(' Quantidade Cara: ',cara_coroa.count('cara'))
print('Quantidade Coroa: ',cara_coroa.count('coroa'))

A = cara_coroa.count('coroa') + cara_coroa.count('cara') 

print('Total de jogadas :' , A)

B = cara_coroa.count('cara') * 100

C = B / A

print('Porcentagem de cara:', "%.1f" % C)

D = cara_coroa.count('coroa') * 100

E = D/A

print('Porcentagem de coroa:', "%.1f" % E)