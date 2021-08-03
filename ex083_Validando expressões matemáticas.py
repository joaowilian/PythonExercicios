'''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com
os parênteses abertos e fechados na ordem correta.

'''

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
