# Exercício Python 014: Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Temperatura em graus Cº: '))
f = (temp * 9/5) + 32
print('{}Cº Equivale a {}Fº'.format(temp,f))