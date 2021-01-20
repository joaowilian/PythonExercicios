from time import sleep

def maior(*num):
    cont = 0
    print('-='*20)
    print('Analisando os valores passados....')
    for x in num:
        print(f'{x}',end=' ')
        cont += 1
        sleep(0.5)
    print(f'\nForam informados {len(num)} valores ao todo.')
    print(f'O maior valor foi {max(num)}')


maior(2,5,83,1,8)
maior(1,2)
maior(1,5,6,5,5,8,2,3)