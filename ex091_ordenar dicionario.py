from random import randint
from operator import itemgetter
jogador = dict()
jogadorOrdenado = list()

for y in range(1,5):
    jogador[f'Jogador {y}'] = randint(1,6)

'''
jogador = {'jogador1': randint(1,6),
           'jogador2': randint(1,6),
           'jogador3': randint(1,6),
           'jogador4': randint(1,6),
    
}
'''
# Mostra na tela
for k,v in jogador.items():
    print(f'O {k} tirou {v}')

jogadorOrdenado = sorted(jogador.items(),key=itemgetter(1),reverse=True)
print('-='*20)
print("Ranking dos jogadores:")

for i , v in enumerate(jogadorOrdenado):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
#print(sorted(jogador.items(),key=itemgetter(1),reverse=True))



