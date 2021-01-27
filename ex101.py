from time import sleep


def contador(i,f,p):
    """
    :param i:er
    :param f:er
    :param p:er
    :return: sser
    """

    c = i
    while c <= f:
        print(f'{c}',end=' ')
        c += p
        sleep(0.2)
    print('FIM!')

help(contador)
