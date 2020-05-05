jogador = dict()
l = list()


print("=-"*30)

jogador['nome'] = input('Qual o nome do jogador: ')

partidas = int(input(f'quantas partidas {jogador["nome"]} jogou: '))
for x in range(partidas):
    l.append(int(input(f'quantos gols na partida {x}? ')))

jogador['gols'] = l[:]
jogador['total'] = sum(l)
print(jogador)
print("=-"*30)

for k, v in jogador.items():
    print(f'O Campo {k} tem valor: {v}')
# print(f'O campo nome tem valor: {jogador["nome"]}')
# print(f'O Campo gols tem valor: {l}')
# print(f'O campo total tem valor: {jogador["total"]}')

print("=-" * 30)

print(f'O Jogador {jogador["nome"]} jogou {len(l)} partidas')
for x ,y in enumerate(l):
    print(f'    ==> Na partida {x}, fez {y} gols.')
print(f'Foi um total de {jogador["total"]} gols.')