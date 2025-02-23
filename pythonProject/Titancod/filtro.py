"""
1
9
3 1 4 1 5 9 2 6 5
"""

casos = int(input())
for _ in range(casos):
    elementosProcesar = int(input())
    cadenaElementos = list(map(int, input().split()))
    suma = 0
    for elemento in cadenaElementos:
        if (elemento * 2) % 3 == 0:
            suma += elemento * 2
    print("La suma es {}".format(suma))
