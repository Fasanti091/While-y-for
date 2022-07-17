#Segundo ejercicio

nombre_usuario = input("Ingrese su nombre: ")
numerox = int(input(f"Hola {nombre_usuario} ingrese un numero impar: "))
    
while (numerox % 2) == 0:
    numerox = int(input(f"El numero ingresado es ({numerox}) y es par. {nombre_usuario} recuerda que tiene que ser impar: "))
else:
    print(f"El numero ingresado es ({numerox}) y es impar. Gracias {nombre_usuario}")