primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
print('-=-' * 20)
c = 1
while c <= 10:
    print(f'{primeiro}, ', end='')
    primeiro += razao
    c +=1
print('Acabou')
print('=-=' * 20)
