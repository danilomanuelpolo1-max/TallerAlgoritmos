nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

prom = (nota1 + nota2 + nota3) / 3

if prom >= 3.0:
    print("Aprobó con:", prom)
else:
    print("Reprobó con:", prom)
