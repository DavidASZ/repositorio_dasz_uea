# Programa para calcular el salario semanal


def calcular_salario(horas_trabajadas, pago_por_hora):
    salario_total = horas_trabajadas * pago_por_hora
    return salario_total


if __name__ == "__main__":
    print("=== CÁLCULO DEL SALARIO SEMANAL ===")

    horas = float(input("Ingrese las horas trabajadas: "))
    pago = float(input("Ingrese el pago por hora: $"))

    resultado = calcular_salario(horas, pago)

    print("\n=== RESULTADO ===")
    print(f"Horas trabajadas: {horas}")
    print(f"Pago por hora: ${pago:.2f}")
    print(f"Salario semanal: ${resultado:.2f}")
