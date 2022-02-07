def aumentar(a=0, b=10):
    a = a * (b / 100 + 1)
    return a


def dobro(a=0):
    a *= 2
    return a


def metade(a=0):
    a /= 2
    return a


def reduzindo(a=0):
    a = a - a * 0.13
    return a


def moeda(p=0, f='R$'):
    return f'{f}{p:.2f}'.replace('.', ',')
