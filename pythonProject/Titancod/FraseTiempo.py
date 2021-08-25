from functools import reduce
import re


def secondsToStr(t):
    return "%02d:%02d:%02d.%02d" % reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(round(t * 1000),), 1000, 60, 60])


eliminarNoLetras = lambda str: "".join(re.findall("[\w]", str))

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
    xmax2 = secondsToStr(xmax)[:-1]
    xmin2 = secondsToStr(xmin)[:-1]
    listaEntradas.append((xmin2, xmax2, text))

for i in range(len(listaEntradas)):

    valor = listaEntradas[i][2]
    if valor != '""' or listaEntradas[i][2] != '""':
        listaSinVacios.append(listaEntradas[i])

todo = len(listaSinVacios) - 1
j = 0

prueba = (listaSinVacios[1][2])
new_string = prueba.replace('"', '')

for i in listaSinVacios:
    print((i[0]))
    print((i[1]))
    og = str(i[2])
    og2 = og.replace('"', '')
    aux = str(eliminarNoLetras(og2))

    # print(aux.lower())

    if og2 == aux:
        og3 = og2.lower()
        if j == todo:
            print(og3, end="")
        elif j < todo:
            print(og3)
            print("")
            j += 1
    else:
        if j == todo:
            print(aux, end="")
        elif j < todo:
            print(aux)
            print("")
            j += 1
