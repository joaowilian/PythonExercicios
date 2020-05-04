from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*40)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-'*40)
quant = int(input('Quantos jogos você quer que eu sorteie?'))
print('')
cont = 0
for x in range(0,quant):
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    cont = 0

for i , l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(0.5)
