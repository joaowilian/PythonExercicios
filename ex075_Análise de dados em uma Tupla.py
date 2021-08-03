t = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um npumero: ')),
    int(input('Digite o último número: ')))

print(f'Voçê digitou os valores {t}')
print(f'O valor 9 apareceu  {t.count(9)} vesez')
if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3)+1}º posição')
else:
    print('O valor 3 nao foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram ')
for x in t:
    if x % 2 == 0:
        print(x ,end=' ')





