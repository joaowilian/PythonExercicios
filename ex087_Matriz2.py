matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = somaColuna = 0
for x in range(0,3):
    for y in range(0,3):
        matriz[x][y] =int(input(f'Digite um valor para [{x},{y}] => '))

for x in range(0,3):
    for y in range(0,3):
        if matriz[x][y] % 2 == 0:
            somapar += matriz[x][y]
    somaColuna += matriz[x][2]

for x in range(0,3):
    for y in range(0,3):
        print(f'[{matriz[x][y]:^6}]',end='')
        # centraliza 6 casas decimais
    print()
print(f'A soma dos valores pares é {somapar} ')
print(f'A soma dos valores d terceira coluna é {somaColuna}')
print(f'O maior valor da sgunda linha é {max(matriz[1])}')