n = 0
cont = 0
soma = 0
while not n == 999:
    n = int(input('Digite numero inteiro:[999 para parar] '))
    if n != 999:
        cont +=1
        soma += n
print(f'Foi digitado {cont} números ')
print(f'A soma de todos os números é {soma}')