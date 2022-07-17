#Cuarto programa

nombre_usuario = input("Ingrese su nombre: ")
intentos = int(input(f"Cuantos numeros vas a escribir {nombre_usuario}: "))
numero_intentos = intentos
suma_muneros = []

while (intentos > 0) and (numero_intentos > 0):
    suma_muneros.append (int(input(f"[ Numero del intento {numero_intentos} ] \nEscribe un numero {nombre_usuario}: ")))
    numero_intentos -= 1

media_aritmética = (sum(suma_muneros) / intentos)

print(f"\n{nombre_usuario} la media aritmética de los numeros ingresados es: \n ----> ", round(media_aritmética,3))
