totalHorasTrabajadas = 0

valorHora = float(input("Ingrese el valor por hora: "))

for i in range(1, 6):
    horasDelDia = float(input(f"Ingrese las horas trabajadas el día {i}: "))
    totalHorasTrabajadas += horasDelDia

salarioBase = totalHorasTrabajadas * valorHora
salarioTotal = salarioBase

if totalHorasTrabajadas > 40:
    horasExtra = totalHorasTrabajadas - 40
    pagoExtra = horasExtra * valorHora * 0.5
    salarioTotal = salarioBase + pagoExtra

print("\n--- Resumen Semanal ---")
print("Total de horas trabajadas:", totalHorasTrabajadas)
print("Salario total:", salarioTotal)
