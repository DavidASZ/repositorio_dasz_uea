# Programa: Reserva de asiento en una sala de cine
# Semana 12 - Fundamentos de Programación

# Crear matriz de 3 filas por 4 columnas inicializada en 0
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar al usuario la fila y la columna
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Marcar el asiento como reservado
asientos[fila][columna] = 1

# Mostrar el estado completo de la sala
print("\nEstado de la sala:")

for i in range(3):
    for j in range(4):
        print(asientos[i][j], end="\t")
    print()