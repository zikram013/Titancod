
partidos = []

while True:
    try:
        linea = input().strip()
        if linea:
            partidos.append(linea)
    except EOFError:
        break

resultados = []  # almacena la cantidad de veces que tuvo mano caliente en cada partido
partidos_con_mano_caliente = 0

for partido in partidos:
    contador = 0
    consecutivos = 0
    for ch in partido:
        if ch == '1':
            consecutivos += 1
        else:
            if consecutivos >= 5:
                contador += 1
            consecutivos = 0
    # Verificar al final de la línea si quedó una secuencia pendiente
    if consecutivos >= 5:
        contador += 1

    resultados.append(contador)
    if contador > 0:
        partidos_con_mano_caliente += 1

# Imprimir el resultado por partido
for res in resultados:
    print(res)

# Calcular y mostrar el porcentaje de partidos con mano caliente
total_partidos = len(partidos)
if total_partidos > 0:
    porcentaje = (partidos_con_mano_caliente / total_partidos) * 100
else:
    porcentaje = 0.0

# Formatear el porcentaje con dos decimales, cambiando el punto por coma.
print("{:.2f}".format(porcentaje).replace('.', ','))

