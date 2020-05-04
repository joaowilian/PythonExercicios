while True:
    t = int(input('Voçê quer ver a tabuada de qual valor? '))
    if t < 0:
        break
    print('--' * 20)
    for c in range(1, 11):
        print(f'{t} x {c} = {c * t}')
    print('--' * 20)
print('Tabuada encerada')



