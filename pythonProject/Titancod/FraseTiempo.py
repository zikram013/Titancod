import string

casosDePrueba = int(input())
listaEntradas = list()
alfa = "abcdefghijklmnopqrstuvwxyz"
alfalist = list(alfa)
pos = 0
listaSinVacios = list()
for i in range(casosDePrueba):
    xmin = float(input())
    xmax = float(input())
    text = input()
    listaEntradas.append((xmin, xmax, text.lower()))

for i in range(len(listaEntradas)):
    print(listaEntradas[i][2])
    valor = listaEntradas[i][2]
    if valor != '""' or listaEntradas[i][2] != '""':
        listaSinVacios.append(listaEntradas[i])

print(listaSinVacios)

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
