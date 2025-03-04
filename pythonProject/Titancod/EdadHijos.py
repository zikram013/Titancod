"""
4
72
30
288
100
"""
def encontrar_edades_producto(edad_producto):
    soluciones = set()
    
    for x in range(1, int(edad_producto ** (1/3)) + 2):
        y = x  # Asegurar que los dos primeros números sean iguales
        if (edad_producto % (x * y)) == 0:
            z = edad_producto // (x * y)
            if z > y:  # Asegurar que el tercer número sea estrictamente mayor
                soluciones.add((x, y, z))
    
    return sorted(soluciones)

# Función principal para resolver el problema
def resolver_edad_hijos():
    num_casos = int(input())  # Leer el número de casos de prueba
    for _ in range(num_casos):
        edad_producto = int(input())  # Leer el producto de las edades
        soluciones = encontrar_edades_producto(edad_producto)
        
        if not soluciones:
            print("*")  # Si no hay soluciones
            continue
        
        suma_edades = {}
        for s in soluciones:
            suma = sum(s)
            if suma in suma_edades:
                suma_edades[suma].append(s)
            else:
                suma_edades[suma] = [s]
        
        # Filtrar las sumas que aparecen más de una vez
        posibles_soluciones = []
        suma_repetida = None
        for suma, combinaciones in suma_edades.items():
            if len(combinaciones) == 1:
                posibles_soluciones.append(combinaciones[0])
            else:
                suma_repetida = suma
        
        # Si no hay soluciones únicas, imprimimos "*"
        if not posibles_soluciones:
            print("*")
        # Si hay exactamente una solución única, la imprimimos
        elif len(posibles_soluciones) == 1:
            print(*posibles_soluciones[0])
        # Si hay múltiples sumas repetidas, devolvemos "+"
        elif suma_repetida is not None:
            print("+")
        else:
            print("+")  # Si aún hay múltiples soluciones, imprimir ""

# Ejecutar el programa
if __name__ == "__main__":
    resolver_edad_hijos()
