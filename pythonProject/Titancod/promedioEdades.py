def calcular_promedio(cadena):
    edades = []
    i = 0
    while i < len(cadena):
        # Si encontramos el patrón "10"
        if cadena[i] == '1' and i + 1 < len(cadena) and cadena[i+1] == '0':
            edades.append(10)
            i += 2
        else:
            edades.append(int(cadena[i]))
            i += 1
    return sum(edades) / len(edades)

t = int(input())
for _ in range(t):
    cadena = input().strip()
    promedio = calcular_promedio(cadena)
    # Si el promedio es entero, se imprime sin decimales; de lo contrario, se redondea a 5 decimales.
    if promedio.is_integer():
        print(int(promedio))
    else:
        print(round(promedio, 5))
