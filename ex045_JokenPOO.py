from random import randint
from time import sleep

op = ["pedra", "papel", "tesoura"]
co = randint(0,2) # computador escolhe entre 0,1,2
print('''
[ 1 ] Pedra
[ 2 ] Papel 
[ 3 ] Tesoura
''')
vc = int(input('Qual sua jogada'))
print('Jo')
sleep(1)
print('ken')
sleep(1)
print('POoo!!')
sleep(1)
print('=-'*20)
print(f'Computador jogou {co}')
print(f'Você jogou {vc}')
print('=-'*20)

if co == 0:
    if vc == 0:
        print('Empatou')
    elif vc == 1:
        print('Jogador Vence')
    elif vc == 2:
        print('Computador Vence')
    else:
        print('jogada invalida')
elif co == 1:
    if vc == 0:
        print('computador vence')
    elif vc == 1:
        print('Empate')
    elif vc == 2:
        print('jogador vence')
    else:
        print('jogada invalida')

elif co == 2:
    if vc == 0:
        print('jogador vence')
    elif vc == 1:
        print('computador vence')
    elif vc == 2:
        print('empate')
    else:
        print('jodagada invalida')