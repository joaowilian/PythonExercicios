primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
print('-=-' * 20)
decimo = primeiro + (10 -1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}, ', end='')
print('Acabou')
print('=-=' * 20)
