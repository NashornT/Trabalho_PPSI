'''Exercicio 3'''



sexo = input('Digite seu sexo (M/F)').strip().upper()[0]
altura = float(input('Digite sua altura:'))

peso_ID_M = float(72.7*altura)-58
peso_ID_F = float(62.1*altura)-44.7

if sexo == 'M':
    print(f'Seu peso ideal seria {peso_ID_M}')
elif sexo == 'F':
    print(f'Seu peso ideal seria {peso_ID_F}')
else:
    print('Ops , você digitou uma opção invalida')

