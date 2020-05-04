soma = 0
for c in range(1, 7):
    n = int(input(f'Digite {c} número: '))
    if n % 2 == 0:
        soma += n
print(f'Soma de todos os números pares = {soma}')