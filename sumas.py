suma = 0

print("=== Suma de números (ingrese 0 para terminar) ===")

num = float(input("Ingrese un número: "))

while num != 0:
    suma += num
    num = float(input("Ingrese otro número (0 para finalizar): "))

print("La suma total de los números ingresados es:", suma)
