frase = str(input('Digite uma frase: ')).strip().upper()
junto = frase.replace(' ','')
inverso = junto[::-1]

# linha acima substitui todo esse codigo comentado

'''
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
'''

print(junto,inverso)
if inverso == junto:
    print('temos um palindromo')
else:
    print('Não e um palindromo')
