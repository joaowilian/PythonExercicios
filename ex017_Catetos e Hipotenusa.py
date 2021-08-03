'''
Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
'''


from math import hypot
c1 = float(input('Informe o comprimento do cateto oposto: '))
c2 = float(input('Informe o comprimento do cateto adjacente: '))
print('o tamanho da hipotenuza e: {:.2f}'.format(hypot(c1,c2)))