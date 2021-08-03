# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.


from math import trunc
num = float(input('digite um número real: '))
print('O número {} possui {} partes inteiras'.format(num,trunc(num)))

''' ou pode ser usado como abaixo

num = float(input('digite um numero real: '))
print('O número {} possui {} parte inteiras'.format(num,int(num)))

'''
