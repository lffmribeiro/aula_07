'''
criar uma lista par e uma lista impar
printar as listas
'''
i = 0
lista_par = []
lista_impar = []

for i in range(0,100):
    if i%2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
    i+=1

print(lista_impar)
print(lista_par)