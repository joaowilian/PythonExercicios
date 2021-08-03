imovel = float(input("Valor do imovel: "))
sal = float(input("Salario: R$ "))
anos = int(input("quantos anos: "))

prestacao = imovel / (anos * 12)

if prestacao <= (sal * 0.3):
    print(f'Aprovado  parcela de R$ {prestacao:.2f}')
else:
    print('Emprestimo Não aprovado')
    print(f'Prestação de {prestacao:.2f} exedeu 30% do salario')
