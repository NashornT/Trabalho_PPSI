'''Exercicio 4'''


salarioH = float(input('Digite o quanto você recebe por Hora:'))
Trab_Hora = float(input('Digite quantas horas trabalho por mês:'))

salarioBruto = salarioH*Trab_Hora

imposto = (salarioBruto*11)/100
Inss = (salarioBruto*8)/100
sind = (salarioBruto*5)/100


salarioLiq = salarioBruto-(imposto+Inss+sind)


print(f'O seu salário Bruto foi de R${salarioBruto} e o liquido foi de R${salarioLiq}\nPagou R${Inss} ao INSS\nPagou R${sind} ao sindicato\n e R${imposto} de imposto')
print('~~'*10)
print(f'IR (11%):R${imposto}')
print(f'INSS (8%):R${Inss}')
print(f'Sindicato (5%):R${sind}')
print(f'Salário Líquido:R${salarioLiq}')
print('~~'*10)
