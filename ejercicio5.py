#Quinto programa

nombre_usuario = input("Ingrese su nombre: ")
numero_usuario = int(input(f"{nombre_usuario} ingrese un numero entero del 0 al 9: "))
numeros = [1,3,6,9]

while (numero_usuario >= 0) and (numero_usuario <= 9):
    if numero_usuario in numeros:
        print(f"Muy bien {nombre_usuario} usted hacerto a los numeros que teniamos en el sistema \nSu numero fue \n----> {numero_usuario} \n[Numeros del sistemas] ")
        for lista_numeros in range(0,len(numeros),1):
            print(f"---> {numeros[lista_numeros]}")
        break
    else:
        pass
    numero_usuario = int(input(f"{nombre_usuario} ingrese otro numero entero del 0 al 9: "))
else:
    print("El numero ingresado es superor a 9 o menor a 0")
print(f"{nombre_usuario} Adios, Muchas gracias")
   