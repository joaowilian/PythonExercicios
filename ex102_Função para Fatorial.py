

def fatorial(f, show = True):
    """
    -> Calcula o Fatorial de um número.
    :param f: o número a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: O valor fatoria do numero f
    """
    fator = 1
    for x in range(f,0,-1):
        if show:
            print(x,end='')
            if x > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        fator = fator * x
    return fator


if __name__ == '__main__':  #executa se for chamado pelo mesmo nome

    #n = int(input('Diga um valor: '))
    #print(f'Fatorial de {n} é {fatorial(n)}')
    help(fatorial)
    print(fatorial(5,show = True))