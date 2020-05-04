# num = []
# for x in range(0, 5):
#     num.append(int(input(f'Digite um valor para posição {x} : ')))
#
# print(f'Voçê digitou os valores {num}')
#
# print(f'O maior número => {max(num)} nas posições ', end='')
# for a, b in enumerate(num):
#     if max(num) == b:
#         print(f'{a}...', end='')
#
# print(f'\nO menor número => {min(num)} nas posições ', end='')
# for a, b in enumerate(num):
#     if min(num) == b:
#         print(f'{a}...', end='')


num = []
maior = []
menor = []

for x in range(0, 5):
    num.append(int(input(f'Digite um valor para posição {x} : ')))


for a, b in enumerate(num):
    if max(num) == b:
        maior.append(a)
    if min(num) == b:
        menor.append(a)

print(f'Voçê digitou os valores {num}')
print(f'O maior número => {max(num)} nas posições {maior}')
print(f'O menor número => {min(num)} nas posições {menor}')
