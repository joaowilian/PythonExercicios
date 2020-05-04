l = []
print('=-'* 10)
while True :
    num = int(input('Digite um número: '))
    if num in l :
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        l.append(num)

    if input('Quer continuar: [S/N] ') in 'nN':
        break

l.sort()
print(l)


