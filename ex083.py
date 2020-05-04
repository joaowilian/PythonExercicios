lista = []

cont = cont2 = 0
a = str(input('Digite a formula: '))

if '(' in a:
    cont = a.count('(')
if ')' in a:
    cont2 = a.count(')')

if cont == cont2:
     print('Expresao valida')
else:
     print('Expressao nao e valida')
