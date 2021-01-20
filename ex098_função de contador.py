from pygame.time import delay


def contator(inicio, fim, passo):

    if passo < 0: passo *= -1
    if passo == 0: passo = 1

    if inicio > fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for x in range(inicio, fim - 1, -passo):
            print(f'{x}', end=' ')
            delay(100)
        print(' Fim!')  # pular de linha

    if inicio < fim :
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for x in range(inicio,fim-1,passo):
            print(f'{x}',end=' ')
            delay(100)
        print(' Fim!')  # pular de linha




print('-=' * 20)
contator(1,10,1)

print('-=' * 20)
contator(10,0,-2)

print('-=' * 20)
print('Agora e sua vez de personalizar a contagem!')
i = int(input('Início ->'))
f = int(input('Fim ---->'))
p = int(input('Passo -->'))
contator(i,f,p)