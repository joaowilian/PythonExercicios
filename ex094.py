pessoa = dict()
plista = list()
media = 0

while True:
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO" Responda apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    plista.append(pessoa.copy())
    if input('Quer continuar? [S/N]').upper()[0] in 'N':
        break

for x in plista:
    media += plista[x]['idade']


print('+='*30)

print(f'Ao todo temos {len(plista)} Pessoas cadastradas.')
print(f'A média de idade é de {media} anos')


print('\n\n')
print(plista)
print(pessoa)
