n = int(input('Informe um numero:  '))
print('''Converter numero para'
[ 1 ] Converter ==> binario
[ 2 ] Converter ==> octal
[ 3 ] Converter ==> hexadecimal''')
op = int(input())

if op == 1:
    print(f'{n} em Binario = {bin(n)[2:]}')
elif op == 2:
    print(f'{n} em octal = {oct(n)[2:]}')
elif op ==3:
    print(f'{n} em hexadecimal = {hex(n)[2:]}')
else:
    print('Opção invalida tente o numero de 1 a 3')