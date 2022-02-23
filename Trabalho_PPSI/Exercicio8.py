'''Exercicio 8'''


from time import sleep


lista = []
count = 0
indice = 1
print('~~'*10)
print('BEM VINDO')
print('~~'*10)
sleep(0.3)
escolha = int(input('(1) - informe as notas\n(-1) - sair:\n'))

if escolha == 1:
    while True:
        count += 1
        nota = float(input(f'informe nota n {indice}°'))
        indice += 1
        lista.append(nota)
        if nota == -1:
            lista.pop(-1)
            count -= 1
            break
print('~~'*20)
print(f'A quantidade de valores lidos foi: {count}')
print(f'Os valores informados foram: {lista}')
print(f'Os valores invertidos:')

for i in reversed(lista):
    print(i)

print(f'A soma foi {sum(lista)}')

media = sum(lista)/count
NewLis = []
NewLis2 = []

print(f'A média foi de {media}')
for i in lista:
    if i > media:
        NewLis.append(i)
print(f'Os valores maiores que a média foram:\n{NewLis}')

for i in lista:
    if i < 7:
        NewLis2.append(i)
print(f'Os valores menores que  7 foram:\n{NewLis2} ')


print('~~'*10)
print('Obrigado , volte sempre')

