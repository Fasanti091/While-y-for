#Primer ejercicio

nombre_usuario = input("Ingrese su nombre: ")
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un segundo numero: "))

opciones = int(input(f"\nNumeros seleccioandos ({numero1}) ({numero2}) \nHola {nombre_usuario} Selecciona una opcion \n ----> 0 pasa sumar \n ----> 1 para restar \n ----> 2 para multiplicar \n ----> 3 para salir del programa \n \n ----> "))

while opciones < 4: 
    
    if opciones == 0:
        suma = numero1 + numero2
        print(f"\nNumeros seleccioandos ({numero1}) ({numero2}). La suma es igual a: \n ----> {suma} \n")
    elif opciones == 1:
        resta = numero1 - numero2
        print(f"\nNumeros seleccioandos ({numero1}) ({numero2}). La resta es igual a: \n ----> {resta} \n")
    elif opciones == 2:
        multiplicacion = numero1*numero2
        print(f"\nNumeros seleccioandos ({numero1}) ({numero2}). La multiplicacion es igual a: \n ----> {multiplicacion} \n")
    elif opciones == 3:
        print(f"Gracias {nombre_usuario} por utilizanos")
        break
    
    opciones = int(input(f"Hola {nombre_usuario} Selecciona otra opcion \n ----> 0 pasa sumar \n ----> 1 para restar \n ----> 2 para multiplicar \n ----> 3 para salir del programa \n \n ----> "))
else:
    print(f"Lo sentimos {nombre_usuario} algo paso, intentaremos solucionarlo ")