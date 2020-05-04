p = float(input('Qual seu peso: '))
a = float(input('qual sua altura: '))
imc = float(p / (a**2))

if imc < 18.5:
    print(f'Imc {imc:.2f}, Abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'Imc {imc:.2f}, Peso ideal')
elif 25 <= imc < 30:
    print(f'Imc {imc:.2f}, Sobrepeso')
elif 30 <= imc < 40:
    print(f'Imc {imc:.2f}, Obesidade')
else:
    print(f'Imc {imc:.2f}, Obesidade Mórbida')

