from random import randint

venceu = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 20)
while True:
    pc = randint(0, 10)
    eu = int(input('Diga um valor: '))
    pi =' '
    while pi not in 'PpIi':
        pi = str(input('Par ou Impar [P/I]')).strip().upper()[0]
    print('--' * 20)
    soma = pc + eu
    print(f'Voçê jogou {eu} e o computador {pc}, Total de {pc + eu} ',end='')
    print("deu par" if soma % 2 == 0 else 'deu impar' )
    if pi in 'Pp':
        if soma % 2 == 0:
            print('VC VENCEU!')
            print('Vamos jogar novamente')
            venceu += 1
        else:
            print('Voçê PERDEU!')
            break
    if pi in 'Ii':
        if soma % 2 == 1:
            print('VC VENCEU!')
            print('Vamos jogar novamente')
            venceu += 1
        else:
            print('Voçê PERDEU!')
            break
print(f'Game OVER! Voçê venceu {venceu}')