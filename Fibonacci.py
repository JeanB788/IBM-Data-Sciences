#Secuencia de fibonacci
#TODO Haz un rango para limitar los elementos de la sucesion
elemento_maximo = input("Ingresa el número de elementos de la sucesión: ")
rango = range(0,int(elemento_maximo))

#TODO Define las variables
sucesion = []
n_0 = 0
n_1 = 1

#TODO Bucle para cambiar los elementos
for i in rango:
    sucesion.append(n_1)
    n_1 += n_0
    n_0 = n_1

print(sucesion)