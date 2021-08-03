resp =  'N'
cont = 0
media = 0
maior = 0
menor = 0
while resp in 'nN':
    n = int(input('\nDigite um número: '))
    cont += 1
    media += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor :
            menor = n
    resp = str(input('Quer sair do programa? [S/N]:  '))


print(f'Media → {media / cont:.1f}')
print(f'Maior numero {maior}')
print(f'Menor número {menor}')