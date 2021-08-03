from time import sleep

sair = False

x1 = int(input('Informe 1° Valor: '))
x2 = int(input('Informe 2° Valor: '))

while not sair:
    op = int(input('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do programa
    >>>> Qual e sua Opção? '''))

    if op == 1:
        print(f'Soma de {x1} + {x2} = {x1 + x2}')
    elif op == 2:
        print(f'Multiplicacao de {x1} X {x2} = {x1 * x2}')
    elif op == 3:
        print(f'Maior número {max(x1,x2)}')
    elif op == 4:
        x1 = int(input('Informe 1° Valor: '))
        x2 = int(input('Informe 2° Valor: '))
    elif op == 5:
        sair = True
    else:
        print('Opção invalida. tente novamente')
    sleep(2)
print('Final')