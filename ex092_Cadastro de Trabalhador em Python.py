from datetime import date

dicionario = dict()

hj = date.today().year


dicionario['salario'] = float(input('Salário:'))
dicionario['nome'] = str(input('Nome:'))
dicionario['idade'] = hj - int(input('Ano de nascimento:'))
dicionario['ctps'] = int(input("Carteira de trabalho (0 não tem):"))



if dicionario['ctps'] != 0:
    dicionario['contratacao'] = int(input('Ano de contratação:'))
    dicionario['salario'] = float(input('Salário:'))
    dicionario['aposentadoria'] = dicionario['idade'] + ((dicionario['contratacao']  - hj ) + 35)



print('=-' * 20)
for k, v in dicionario.items():
    print(f'   - {k} tem o valor: {v}')

