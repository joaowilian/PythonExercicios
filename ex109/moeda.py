def aumentar(a=0, b=10, f=False):
    a = a * (b / 100 + 1)

    return a if f is False else moeda(a)


def dobro(a=0, f=False):
    a *= 2
    return a if f is False else moeda(a)


def metade(a=0, f=False):
    a /= 2
    return a if not f else moeda(a)


def reduzindo(a=0, f=False):
    a = a - a * 0.13
    return a if not f else moeda(a)


def moeda(p=0, f='R$'):
    return f'{f}{p:.2f}'.replace('.', ',')
