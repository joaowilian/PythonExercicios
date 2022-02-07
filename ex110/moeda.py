def resumo(preco=0, aumento=10, reducao=5):
    print('--'*15)
    print(f'RESUMO DO VALOR'.center(30))
    print('--'*15)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco)}')
    print(f'Metade do preço: \t{metade(preco)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco)}')
    print(f'{reducao}% de redução: \t{reduzindo(preco)}')
    print('--'*15)


def aumentar(a=0, b=10, f=True):
    a = a * (b / 100 + 1)
    return a if not f else moeda(a)


def dobro(a=0, f=True):
    a *= 2
    return a if f is False else moeda(a)


def metade(a=0, f=True):
    a /= 2
    return a if not f else moeda(a)


def reduzindo(a=0, f=True):
    a = a - a * 0.13
    return a if not f else moeda(a)


def moeda(p=0, f='R$'):
    return f'{f}{p:.2f}'.replace('.', ',')
