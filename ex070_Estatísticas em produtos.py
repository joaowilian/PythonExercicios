
print('--'*20)
print(f'{"Loja super BARATÃO":^40}')
print('--'*20)

barato =''
total = quant = cont = menor = 0
while True:
    nome = str(input('Nome Produto: '))
    preco = float(input('Preço R$ '))
    op = ' '
    total += preco
    if preco > 1000:
        quant += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if op in 'N':
        break
print(f'Total gasto na compra R$ {total:.2f}')
print(f'Quantidade de produtos acima de R$ 1000,00: {quant}')
print(f'Nome do produto mais Barato e : {nome} que custa {menor}')

