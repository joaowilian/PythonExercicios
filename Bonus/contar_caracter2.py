
def contarCaracter(s):

    caracter = list(s.upper())
    ss = []

    for p, v in enumerate(caracter):
        cont = caracter.count(v)
        if not v in ss:
            ss.append(cont)
            ss.append(v)

    print(''.join(map(str, ss)))


contarCaracter('BBBBBBBaaBBBBBBAACCcDD')
