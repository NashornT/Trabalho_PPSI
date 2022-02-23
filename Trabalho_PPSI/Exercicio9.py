'''Exercicio 9'''


salarios = [200,260,340,410,570,620,780,810,945,1000,1050]
array_contagen = [0]*9
for x in salarios:
    ind = x//100 - 2
    ind_max = len(array_contagen) -1
    ind_min = min(ind,ind_max)

    array_contagen[ind] += 1
    
print(array_contagen)

