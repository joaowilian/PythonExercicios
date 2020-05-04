p = float(input('preço a pagar: R$'))
op = int(input('''
[ 1 ] A vista Dinheiro
[ 2 ] A vista Cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais
'''))

if op == 1:
    print(f'Valor de R${p - p * 0.1:.2f }, 10% de desconto.')
elif op == 2:
    print(f'Valor de R${p - p * 0.05:.2f }, 5% de desconto')
elif op == 3:
    print(f'Valor de R${p}')
elif op == 4:
    print(f'Valor de R${p * 1.20:.2f}, 20% juros')
else:
    print('Digite uma opção valida')

