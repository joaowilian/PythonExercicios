n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a media do aluno é {media:.1f}')
if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media < 6.9:
    print('Recuperação')
else:
    print('Aprovado')

