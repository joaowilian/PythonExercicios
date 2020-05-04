lista = list()
print('Digite -1 para sair')
print('-='*10)
while True:
    n = int(input("Digite um número "))
    if n == -1:
        break
    elif n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    lista.append(n)
print(F'lista com todos os números =>{lista}')
print(F'lista com números pares ====>{par}')
print(F'lista com números impares  =>{impar}')