lista = []

for x in range(5):
    num = int(input(f'Digite {x + 1} valor númerico: '))
    if x == 0 or num > lista[-1]:  # lista[-1] pega o ultimo valor
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                break
            pos += 1


print(lista)
