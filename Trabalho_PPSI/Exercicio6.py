'''Exercicio 6'''


salario = float(input('Informe seu salário:'))
ajuste = (salario*20)/100
NewSala = salario + ajuste 

if salario <= 280.00:
    print('~~'*20)
    print(f'Salário antes do reajuste R${salario}\nO percentual de aumento aplicado foi de 20%')
    print(f'O valor do aumento foi de R${ajuste}\nNovo salário: R${NewSala}')
    print('~~'*20)
elif salario > 280.00 and salario < 700.00:
    print('~~'*20)
    print(f'Salário antes do reajuste R${salario}\nO percentual de aumento aplicado foi de 15%')
    print(f'O valor do aumento foi de R${ajuste}\nNovo salário: R${NewSala}')
    print('~~'*20)
elif salario > 700.00 and salario < 1500.00:
    print('~~'*20)
    print(f'Salário antes do reajuste R${salario}\nO percentual de aumento aplicado foi de 10%')
    print(f'O valor do aumento foi de R${ajuste}\nNovo salário: R${NewSala}')
    print('~~'*20)
elif salario > 1500.00:
    print('~~'*20)
    print(f'Salário antes do reajuste R${salario}\nO percentual de aumento aplicado foi de 5%')
    print(f'O valor do aumento foi de R${ajuste}\nNovo salário: R${NewSala}')
    print('~~'*20)

