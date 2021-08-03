from datetime import date
a = int(input('Ano de nascimento: '))
id = int(date.today().year -a)
if id < 18:
    print(f' Falta {18 - id} anos para poder se alistar')
elif id > 18:
    print(f' Passou {id -18} anos de se alistar')
else:
    print(f'com {id} ja pode se alistar')