def contar_caracter(s):
    caracter_ordenados = list(s)

    caracter_anterior = caracter_ordenados[0]
    contagem = 1

    for caracter in caracter_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1

    print(f'{caracter_anterior}: {contagem}')


if __name__ == '__main__':
    contar_caracter('BBBBBBBBBBBBBAACCCDD')
