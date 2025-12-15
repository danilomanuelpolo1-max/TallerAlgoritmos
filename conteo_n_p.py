positivos = 0
negativos = 0

for i in range(1, 6):
    num = float(input("Ingrese un número: "))
    
    if num >= 0:
        positivos += 1
    else:
        negativos += 1

print("Positivos:", positivos, " Negativos:", negativos)
