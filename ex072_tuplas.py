
num = ('zero','um' ,'dois' ,'tres' ,'quatro' ,'cinco' ,'seis' ,'sete' ,'oito' ,'nove',
       'dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito',
       'dezenove','vinte')
n = int(input('Digite um número de 0 a 20: '))
while not n >= 0 or  not n <= 20:
    n = int(input('Tente novamente, Digite um número de 0 a 20: '))
print(f'Voçê digitou {num[n]}')
