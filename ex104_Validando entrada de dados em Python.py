def leiaInt(num):
    while True:
        n = input(str(num))

        if not n.isnumeric():
            print( '\033[1;31mERRO! Digite um número válido.\033[m')
        else:
            break
    return n


n = leiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}')
