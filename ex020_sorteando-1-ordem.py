#import random
from random import shuffle
'''
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
'''
n1 = 'joao'
n2 = 'wilian'
n3 = 'pereira'
n4 = 'adriana'
lista = [n1,n2,n3,n4]
shuffle(lista)

print("Ordem escolhida: {}".format(lista))