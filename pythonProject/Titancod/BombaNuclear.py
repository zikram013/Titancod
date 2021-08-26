def atacar(coordenadas, ataX, ataY, radio):
    """
    tuplaAtaquePosX = (ataX + radio, ataY)
    tuplaAtaquePosY = (ataX, ataY+radio)
    tuplaAtaqueMenX = (ataX - radio, ataY)
    tuplaAtaqueMenY = (ataX, ataY - radio)
    """
    contador=0
    for i in coordenadas:
        x=i[0]
        y=i[1]
        if(x*x+y*y)<=radio*radio:
            contador+=1
    return contador


casos = int(input())
for i in range(casos):
    nCoordenadas = int(input())
    listaCoordenadas = list()
    for j in range(nCoordenadas):
        x, y = map(int, input().strip().split())
        listaCoordenadas.append((x, y))
    xa, ya, r = map(int, input().strip().split())
    resultado = atacar(listaCoordenadas, xa, ya, r)
    print(resultado)


"""
3
2
1 1
1 0
0 0 1
2
1 1
1 0
0 0 5
2
0 0
50 50
5 5 10
"""