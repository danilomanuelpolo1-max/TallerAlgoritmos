valorcompra = float(input("Ingrese el valor de la compra: "))

if valorcompra > 100000:
    descuento = valorcompra * 0.1
else:
    descuento = 0

valorfinal = valorcompra - descuento

print("Valor total a pagar: $", valorfinal)
