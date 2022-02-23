'''Exercicio 5'''

nota1 = float(input('1° nota:'))
nota2 = float(input('2° nota:'))

media = (nota1+nota2)/2

if media >= 7.0 and media < 10.0:
    print('\033[33m você foi aprovado.\033[m')
elif media < 7.0:
    print('\033[31mInfelizmente você foi reprovado.\033[m')
elif  media == 10.0:
    print('\033[32m Parabéns você foi aprovado com distinção. \033[m')
