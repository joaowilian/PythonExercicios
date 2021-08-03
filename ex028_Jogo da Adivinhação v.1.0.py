'''
ercício Python 028: Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
n = randint(1,5)
#print(n)
u = int(input('Adivinhe o numero: '))
if n == u:
    print('Vc ganhou 10 Pontos')
else:
    print('Errrooouuu pague 10 flexoes')