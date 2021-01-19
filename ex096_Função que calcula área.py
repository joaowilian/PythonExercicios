def area(l,c):
    print(f'A area do terreno {l} x {c} é de {l * c}m')


print('-- terreno --')
largura = float(input('Informe a largura (m) -->'))
comprimento = float(input('informe o comprimento (m) -->'))

area(largura, comprimento)