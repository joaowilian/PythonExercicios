'''
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

'''

valor = int(input('Valor a ser sacado? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-'*30)



'''
n = int(input('Valor a ser sacado? R$'))

n50 = n // 50
n20 = (n % 50) // 20
n10 = ((n % 50) % 20) // 10
n1 = (((n % 50) % 20) % 10) // 1


print(f'Total de {n50} cédulas de R$ 50')
print(f'Total de {n20} cédulas de R$ 20')
print(f'Total de {n10} cédulas de R$ 10')
print(f'Total de {n1} cédulas de R$ 1')




valor = int(input("informe o valor a ser sacado : "))
nota50 = valor // 50
valor %=  50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")
'''