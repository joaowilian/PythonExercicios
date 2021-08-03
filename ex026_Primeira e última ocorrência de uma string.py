f = input('fraze: ').lower().strip()
print('a' in f)

print(f'Quantidade de letra a aparece: {f.count("a")}')
print('A primeira letra "A" esta na posição: {}'.format(f.find('a')+1))
print('A ultima letra "A" esta na posição: {}'.format(f.rfind('a')+1))