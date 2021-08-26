def fibo(n):
    a, b = 0, 1
    cadena = str(a)
    while a < n:
        a, b = b, a + b
        cadena = cadena + str(a)
    return cadena

mes, dia = map(int, input().strip().split())
cadena = fibo(30)
listaValido = list()
dia = str(dia)
lenDia = len(dia)
mes = str(mes)
lenMes = len(mes)
mesDia = mes + dia
mesDiacortado = ""
if len(mesDia) == 4:
    mesDiacortado = mesDia[:-1]

if len(mesDia) < 3:
    print("NO")
elif len(mesDia) > 4:
    print("NO")
else:
    if mesDia in cadena:
        print("SI")
    else:
        print("NO")

"""
if len(mesDia) == 3:
    if mesDia in cadena:
        print("SI")
    else:
        print("NO")
else:
    if mesDia in cadena or mesDiacortado in cadena:
        print("SI")
    else:
        print("NO")
"""
