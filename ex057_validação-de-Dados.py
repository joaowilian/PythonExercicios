s = str(input('Qual o sexo [M/F]: ').strip()[0])
while s not in 'MmFf':
    s = str(input(print('Dados invalidos.informe o sexo: ')))
print(f'Sexo {s} registrado com sucesso')

