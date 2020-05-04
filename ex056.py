media = 0
contm  = 0

idmaior = 0
nomeHV = '' #nome do homem mais velho
for c in range(1,5):
    print(f'--------{c}° Pessoa ------')
    nome = str(input('Qual seu nome: ').strip())
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo [M/F]: ').upper())
    media += idade

    if sexo == 'F' and idade <= 20:
        contm += 1
    if sexo == 'M' and idade > idmaior:
        nomeHV = nome

print('-=-'*20)
print(f'Quantidade de mulheres com menos de 20 anos é {contm}')
print(f'A media de idade do grupo é {media/4}')
print(f'O nome do homen mais velho é: {nomeHV}\n')