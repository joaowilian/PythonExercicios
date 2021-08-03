primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
print('-=-' * 20)
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{primeiro}, ', end='')
        primeiro += razao
        cont += 1
    print('PAUSE')
    mais = int(input('Que mostrar mais quantos termo: '))
print(f'Acabou com {total} Termos mostrado')
print('=-=' * 20)
