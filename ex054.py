from datetime import date
totmaior = 0
totmenor = 0
x = 0
print(date.today().year)
for n in range(1,8):
    x = int(input(f'{n}º Idade: '))
    if date.today().year - x >= 21:
        totmaior += 1
    else:
        totmenor += 1

print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')
