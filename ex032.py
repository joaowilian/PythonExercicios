from datetime import date
x = int(input('Ano: '))
if x == 0:
    x = date.today().year
if x % 4 == 0 and x % 100 != 0 or x % 400 ==0:
    print(f'{x} é Bissexto')
else:
    print(f'{x} Não e bissexto')