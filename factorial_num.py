n = int(input("Ingrese un número: "))

factorial = 1

if n < 0:
    print("No se puede calcular el factorial de un número negativo.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print("El factorial de", n, "es:", factorial)
