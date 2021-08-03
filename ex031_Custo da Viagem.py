x = int(input('Quantos km e sua viagem: '))
if x >= 200:
    print('Preço da viagem: {:.2f}'.format(0.45 * x))
else:
    print(f'Preço da viagem: {0.50 * x:.2f}')