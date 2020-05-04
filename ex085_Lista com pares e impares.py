num = [[],[]]

for x in range(1,8):
    n = int(input(f"Digite {x}° valor númerico: "))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print("--"*30)
num[0].sort()
num[1].sort()
print(f'Os números pares digitados foram ==>  {num[0]}')
print(f'Os números impares digitados foram => {num[1]}')
