def escreva(msg):
    tam = len(msg) +4
    print('~' *tam)
    print('  '+msg)
    print('~' *tam)


while True:

    f = input('Escreva uma frase, ou (sair) ==> ')


    if f == 'sair':
        break
    escreva(f)