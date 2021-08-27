def comparacion(c1, c2):
    tam = len(c1)
    contador = 0
    for i in range(tam):
        if c1[i] != c2[i]:
            contador += 1
    return contador


casos = int(input())
for i in range(casos):
    c1, c2 = map(str,input().strip().split())
    resultado = comparacion(c1, c2)
    print(resultado)
