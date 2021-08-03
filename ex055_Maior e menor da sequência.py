
peso = float(input('Qual seu peso: '))
pmenor = peso
pmaior = peso
for c in range(1, 5):
    peso = float(input('Qual seu peso: '))
    if peso >= pmaior:
        pmaior = peso
    else:
        pmenor = peso

print(f'O maior peso e {pmaior}')
print(f'O menor peso e {pmenor}')
