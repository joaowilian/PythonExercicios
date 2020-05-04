t = ('aprender', 'programar', 'linguagem', 'python',
     'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
     'mercado', 'trabalhador', 'futuro')
print('--'*20)
print(f'{"VOGAIS":^40}')
print('--'*20)
for p in t:
    print(f'\n{p.upper():.<15} Temos ==> ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}',end=' ')

