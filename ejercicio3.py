#Tercer ejercicio
nombre_usuario = input("Ingrese su nombre: ")
suma_impares = 0

for z in range(1,100,2):
    suma_impares += z

print(f"Hola {nombre_usuario} La suma de los numeros impares del 0 al 100 es: \n ----> {suma_impares}")
