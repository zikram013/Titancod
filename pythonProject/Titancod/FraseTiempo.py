from datetime import timedelta
import re

# timeformat = [str(timedelta(seconds=0.34))]
# print(timeformat)
eliminarNoLetras = lambda str: "".join(re.findall("[\w]", str))


casosDePrueba = int(input())
listaEntradas = list()
alfa = "abcdefghijklmnopqrstuvwxyz"
alfalist = list(alfa)
pos = 0
listaSinVacios = list()
for i in range(casosDePrueba):
    xmin = input()

    xmax = input()

    text = input()
    xmax2 = [str(timedelta(seconds=float(xmax)))]
    xmin2 = [str(timedelta(seconds=float(xmin)))]
    listaEntradas.append((xmin2, xmax2, text.lower()))

for i in range(len(listaEntradas)):

    valor = listaEntradas[i][2]
    if valor != '""' or listaEntradas[i][2] != '""':
        listaSinVacios.append(listaEntradas[i])

for i in listaSinVacios:
    print(str(i[0]))
    print(str(i[1]))
    print(str(eliminarNoLetras(i[2])))



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
""
"""
