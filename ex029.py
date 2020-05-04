v = float(input('Qual velocidade do carro: '))
if v > 80:
    print('Vc foi multado kkk')
    print(f'Valor da multa: R$ {(v-80)*7:.2f}')
else:
    print('Voçè dirige igual uma velha ')