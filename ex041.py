from datetime import date
a = int(input('Data de nascimento: '))
id = date.today().year - a
if id <= 9:
    print('Mirim')
elif id <= 14:
    print('infantil')
elif id <= 19:
    print('junior')
elif id <= 20:
    print('senior')
else:
    print('Master')
