lista = list()
nota = []
nome = []
while True:
    nome = (input('nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])

    print(lista)

    if input("Quer continuar [S/N]: ") in 'nN':
        break
print('-=-' * 20)
print(f'{"No":<4} {"Nome":<10} {"Média":>8}')

for i, l in enumerate(lista):
    print(f'{i:<4} {l[0]:<10} {l[2]:>8.1f}')
print('=-=' * 20)
while True:
    opc = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
