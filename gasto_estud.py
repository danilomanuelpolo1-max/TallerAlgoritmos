dias_semana = 6

pasaje_diario = float(input("Ingrese el gasto diario en pasajes: "))
refrigerio_diario = float(input("Ingrese el gasto diario en refrigerio: "))

gasto_diario_total = pasaje_diario + refrigerio_diario

gasto_semanal = gasto_diario_total * dias_semana

print("\n--- Resultado ---")
print("El gasto diario total es: $", gasto_diario_total)
print("El total semanal gastado (de lunes a sábado) es: $", gasto_semanal)
