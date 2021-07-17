from datetime import date


def voto(n):
    idade = int((date.today().year) - n)
    if idade >= 65:
        print(f'Com {idade} ano: VOTO OPICIONAL')
    elif idade >= 18:
        print(f'Com {idade} ano: VOTO OBRIGATORIO')
    else:
        print(f'Com {idade} ano: NÂO VOTA')


ano = int(input(f'Em que ano você nasceu ?'))
voto(ano)
