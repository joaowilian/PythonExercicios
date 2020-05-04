print('-=-'*20)
print('Analizador de Triangulo')
print('-=-'*20+'\n')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3  and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nOs segmentos acima PODEM FORMAR UM TRIANGULO')
else:
    print('\nOs segmento acima NÃO PODEM FORMAR UM TRIANGULO')
