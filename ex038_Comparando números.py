n1 = int(input('1 número: '))
n2 = int(input('2 número: '))

if n1 > n2:
    print(f'{n1} e maior que {n2}')
elif n2 > n1:
    print(f'{n2} e maior que {n1}')
else:
    print('Os dois números são iguais')
