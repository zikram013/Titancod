def comprobar(respuestas, secuencias):
    contador = 0
    for i in range(len(respuestas) - 1):
        if respuestas[i] == secuencias[i]:
            contador += 1
    return contador


def mostrarSolucion(listaSoluciones):
    print(max(listaSoluciones))
    pos = listaSoluciones.index(max(listaSoluciones))
    if listaSoluciones[0] == listaSoluciones[1] == listaSoluciones[2]:
        print("Alvaro")
        print("Edwin")
        print("Gabriel")
    elif listaSoluciones[0] == listaSoluciones[1]:
        print("Alvaro")
        print("Edwin")
    elif listaSoluciones[0] == listaSoluciones[2]:
        print("Alvaro")
        print("Gabriel")
    elif listaSoluciones[1] == listaSoluciones[2]:
        print("Edwin")
        print("Gabriel")
    elif pos == 0:
        print("Alvaro")
    elif pos == 1:
        print("Edwin")
    elif pos == 2:
        print("Gabriel")


casos = int(input())
secuencias = {
    "Alvaro": ["A", "B", "C", "A", "B", "C", "A", "B", "C"],
    "Edwin": ["B", "A", "B", "C", "B", "A", "B", "C", "B", "A", "B", "C"],
    "Gabriel": ["C", "C", "A", "A", "B", "B", "C", "C", "A", "A", "B", "B"]
}



for i in range(casos):
    listasSoluciones = list()
    preguntas = int(input())
    respuestas = input()
    for i in secuencias:
        # print(secuencias.get(i))
        isec = secuencias.get(i)
        # print(isec)
        solucion = comprobar(respuestas, isec)
        listasSoluciones.append(solucion)
    mostrarSolucion(listasSoluciones)

"""
2
5
BAACC
9
AAAABBBBBB
"""
