pessoas = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    # [:] Faz uma copia da lista temp e coloca no primeiro campo
    # da lista pessoas, ficando uma lista dentro da outra lista

    op = input('Quer continuar [S/N]?').upper()
    temp.clear() # apaga lista temp
    if op == 'N':
        break
print('-='*25)
print(f'Ao todo, voçê cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}Kg. ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
print(f'\nO menor peso foi de {menor}Kg. ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')