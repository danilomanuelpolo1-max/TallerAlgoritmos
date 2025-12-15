contadorMayor = 0
contadorMenor = 0
hayMasUsuarios = True

while hayMasUsuarios:
    print("\n--- Nuevo Usuario en la Fila ---")
    
    edad = int(input("Ingrese la edad del usuario (o ingrese 0 si ya no hay más personas en la fila): "))
    
    if edad == 0:
        hayMasUsuarios = False
    else:
        if edad >= 18:
            contadorMayor += 1
            print(f"Edad: {edad} -> MAYOR de edad. Puede INGRESAR al evento.")
        else:
            contadorMenor += 1
            print(f"Edad: {edad} -> MENOR de edad. NO puede ingresar al evento.")
    
    print()

print("______________________________________________")
print("FIN DE LA FILA - REPORTE DE INGRESO")
print("----------------------------------------------")
print("Total de personas mayores (>= 18):", contadorMayor, ". PUEDEN INGRESAR.")
print("Total de personas menores (< 18):", contadorMenor, ". NO PUEDEN INGRESAR.")
print("Total de personas procesadas:", contadorMayor + contadorMenor)
print("______________________________________________")
