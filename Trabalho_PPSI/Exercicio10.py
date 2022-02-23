'''Exercicio 10'''



from time import sleep



prestacoes = []

def valorPagamento():
    
    count = 0   
   
    while True:

        prestacao = float(input('informe o valor da prestação:'))

        if prestacao == 0:
            break

        perg = input('Há pagamento atrasado ? (S/N)').strip().upper()[0]

        if perg == 'S':
            NumDias = int(input('informe quantos dias o pagamento está atrasado:'))
            valor = prestacao + (prestacao*3)/100 + (1/100)*NumDias
            prestacoes.append(valor)
            print('~~'*15)
            print(f'R${valor}')
            count += 1

        elif perg == 'N':
            valor = prestacao
            prestacoes.append(valor)
            print('~~'*15)
            print(f'R${valor}')
            count += 1
    
    print('~~'*15)
    print('Exibindo relatório do dia... ')
    sleep(0.5)
    print(f'Total de prestações pagas {count}')
    for i in prestacoes:
        print(f'R${i}')

    print(f'Valor total pago R${round(sum(prestacoes),2)}')
    print('~~'*15)


valorPagamento()