print('--' * 20)
print('Cadastrar usuario')
print('--' * 20)
cont18 = contF = contM = 0
while True:
    id = int(input('Qual sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [M/F]: ')).upper()[0]
    if id > 18:
        cont18 += 1
    if sexo in 'M':
        contM += 1
    elif id < 20:
        contF += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Cadastrar mais pessoas? [S/N]: ')).upper()[0]
    if op in 'Nn':
        break
    print('--' * 20)
print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Ao todo temos {contM} cadastrados.')
print(f'Tem {contF} mulheres com menos de 20 anos.')