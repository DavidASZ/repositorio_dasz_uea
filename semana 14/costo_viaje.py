# Programa para calcular el costo de combustible de un viaje David Silva

def calcular_costo_viaje(distancia, rendimiento, precio_combustible):
    litros_necesarios = distancia / rendimiento
    costo_total = litros_necesarios * precio_combustible
    return costo_total


print("=== CÁLCULO DEL COSTO DE UN VIAJE ===")

distancia = float(input("Ingrese la distancia del viaje en kilómetros: "))
rendimiento = float(input("Ingrese el rendimiento del vehículo en km/litro: "))
precio_combustible = float(input("Ingrese el precio de un litro de combustible: $"))

resultado = calcular_costo_viaje(
    distancia,
    rendimiento,
    precio_combustible
)

print(f"\nEl costo estimado de combustible es: ${resultado:.2f}")