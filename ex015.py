km = float(input('Quantos km percorrido: '))
dias = int(input('Quantos dias?: '))
preco = (60 * dias) + (0.15 * km)
print(f'Valor total a pagar  R${preco:.2f}')
