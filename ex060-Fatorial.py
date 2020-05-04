#from math import factorial


n = int(input('Digite um número: '))
c = n


f = 1
while c > 0:
    f = f * c
    c -= 1


print(f)
