"""
8
0
0.34
""
0.34
1.35
"TIWULAMPITA."
1.35
2.57
"KUSIKUSIMPITA"
2.57
2.97
""
2.97
3.73
"kuntiri:"
3.73
4.26
"alicia"
4.26
4.79
"ramos"
4.79
4.80
" "
"""

numeroCasos = int(input())
listaCasosInitTime = []
listaCasosFinishTime = []
listaCasosPalabra =[]


def convertirTiempo(time):
    horas = int(time // 3600)
    minutos = int((time % 3600) // 60)
    restoSegundos = time % 60
    return f"{horas:02d}:{minutos:02d}:{restoSegundos:05.2f}"


for i in range(numeroCasos):
    timeInit = float(input().strip())
    timeFinal = float(input().strip())
    timePalabra = input().strip('"')
    if len(timePalabra) > 0:
        print(convertirTiempo(timeInit))
        print(convertirTiempo(timeFinal))
        palabra = timePalabra.lower()
        print(palabra)
        print("")

