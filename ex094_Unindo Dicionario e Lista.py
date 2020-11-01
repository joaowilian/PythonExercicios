pessoa = dict() # pode ser declado --> pessoa = {}
plista = list() # pode ser declado --> plista = []
media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ') ).upper()[0]# .upper()[0]  --> coloca em maiusculo e pega a 1 letra
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO" Responda apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    plista.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO" Responda apenas M ou F')
    if resp == 'N':
        break

# calcula a media
for x in plista:
    media += x['idade']
media = media/len(plista)


print('+='*30)
print(f'A) Ao todo temos {len(plista)} Pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for x in plista:
    if x['sexo'] in "F":
        print(f'{x["nome"]} ',end='')
print()

print(f'D) Lista das pessoas que estão acima da média:')
for x in plista:
    if x['idade'] > media:
        print(f'    nome = {x["nome"]}; sexo = {x["sexo"]}; idade = {x["idade"]}')

print('<< ENCERRADO >>')

