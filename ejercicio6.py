#Sexto programa parte 1

lista1_numeros = []
lista2_numeros = []
lista3_numeros = []
lista4_numeros = []
lista5_numeros = []
invertidos = []

for x in range(0,11):
    lista1_numeros.append(x)
for x in range(0,11):
    invertidos.append(x * -1)
    lista2_numeros = invertidos[::-1]
for x in range(0,21): 
    if x % 2 == 0:
        lista3_numeros.append(x)
for x in range(0,21):
    if x == 0:
        invertidos.clear()
    elif not(x % 2 == 0):
        invertidos.append(x * -1)
        lista4_numeros = invertidos[::-1]
for x in range(0,51):
    if x % 5 == 0:
        lista5_numeros.append(x)

print(f"[Todos los números del 0 al 10] \n ----> {lista1_numeros} \n[Todos los números del -10 al 0] \n ----> {lista2_numeros} \n[Todos los números pares del 0 al 20] \n ----> {lista3_numeros} \n[Todos los números impares entre -20 y 0] \n ----> {lista4_numeros} \n[Todos los números múltiples de 5 del 0 al 50] \n ----> {lista5_numeros}")


#Sexto programa parte 2

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []

for x in lista_1:
    if x in lista_1 and x in lista_2:
        if not x in lista_3: 
            lista_3.append(x)

print(f"Lista 3 ----> {lista_3}")
