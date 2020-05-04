matriz = [[0,0,0],[0,0,0],[0,0,0]]
for x in range(0,3):
    for y in range(0,3):
        matriz[x][y] =int(input(f'Digite um valor para [{x},{y}] => '))

for x in range(0,3):
    for y in range(0,3):
        print(f'[{matriz[x][y]:^6}]',end='')
        # centraliza 6 casas decimais
    print()