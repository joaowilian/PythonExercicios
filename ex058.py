from random import randint

computador = randint(0, 10)
print('''
Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que voçê consegue adivinhar qual foi?
''')
cont = 0
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite: '))
    cont += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente mais uma vez.')
        else:
            print('Mais... Tente mais uma vez.')
print(f'Acertou em {cont} tentativas. Parabéns')
