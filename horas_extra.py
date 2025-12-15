horasTrabajadas = float(input("Ingrese las horas trabajadas: "))
valorHora = float(input("Ingrese el valor por hora: "))

salario = horasTrabajadas * valorHora

if horasTrabajadas > 40:
    horas_extra = horasTrabajadas - 40
    extra = horas_extra * valorHora * 0.5
    salario += extra
    print(f"Horas extra: {horas_extra} (pagadas al 50%)")

print("Salario total:", salario)
