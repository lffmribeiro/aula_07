'''
criar uma lista par e uma lista impar
printar as listas

33, 61, 83
'''
i = 0
lista_par = []
lista_impar = []

for i in range(0,101):
    if i%2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
    i+=1

for nun in lista_impar:
    if nun in {33, 61, 88}:
        print(f"Na lista impar eles estão na posicao {lista_impar.index(nun)}")
for nun in lista_par:
    if nun in {33, 61, 88}:
        print(f"Na lista par eles estão na posicao {lista_par.index(nun)}")

print(lista_impar)
print(lista_par)