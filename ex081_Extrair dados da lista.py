print(f'--' * 10)
print('Digire -1 para sair')
print(f'--' * 10)
l = []
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    l.append(n)

print(f'Voçê digitou {len(l)} números')
print(f'Os valores em ordem decrescente são {sorted(l,reverse=True)}')

if 5 in l:
    cont = l.count(5)
    print(f'O valor 5 faz parte da lista! apareceu {cont}')
else:
    print('O valor 5 não foi encontrado na lista')
