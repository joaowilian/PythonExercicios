from random import randint
from time import sleep

numeros = list()


def sorteia(num):
    print(f'Sorteando 5 valores --> ', end='')
    for x in range(5):
        n = randint(1, 10)
        num.append(n)
        sleep(0.5)
        print(n, end=' ')
    print('PRONTO!')


def somaPar(num):
    soma = 0
    for x in num:
        if x % 2 == 0:
            soma += x
    print(f'Somando valores pares de {num}, temos --> {soma}')


sorteia(numeros)
somaPar(numeros)
