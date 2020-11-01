jogador = dict()
time = list()
l = list()

print("=-"*30)

while True:
    jogador.clear()
    jogador['nome'] = input('Qual o nome do jogador: ')
    l.clear()
    partidas = int(input(f'quantas partidas {jogador["nome"]} jogou: '))
    for x in range(partidas):
        l.append(int(input(f'quantos gols na partida {x+1}? ')))

    jogador['gols'] = l[:]
    jogador['total'] = sum(l)
    time.append(jogador.copy())
    print(jogador)
    print("=-"*30)

    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas Sim ou Não')
    if resp =='N':
        break
print(time)
print()

# mostra o cabeçalho da tabela
print('-'*50)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*50)


# mostra a tabela de jogadores
for k, v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print()

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!  Não existe jogador com código{busca}!')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}!')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('+'*50)
