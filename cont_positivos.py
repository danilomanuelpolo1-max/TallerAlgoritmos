contador_positivo = 0
numero_ingresado = 1 

while numero_ingresado != 0:
    numero_ingresado = int(input("Ingrese un número (ingrese 0 para finalizar): "))

    if numero_ingresado > 0:
        contador_positivo += 1

print("_____________")
print("Se ingresaron", contador_positivo, "números positivos")
print("Algoritmo finalizado")
