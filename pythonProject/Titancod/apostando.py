def apu(listas, apuestas, difGoles):
    if apuestas == 3:
        if difGoles == 0:
            gananciaNeta = listas[0][1] + listas[0][2]
            gananciaPersona = listas[0][0] * listas[1][0]
            return gananciaNeta * 100 - gananciaPersona
        elif difGoles == 1:
            gananciaNeta = listas[0][0] + listas[0][2]
            gananciaPersona = listas[0][1] * listas[1][1]
            return gananciaNeta * 100 - gananciaPersona
        else:
            gananciaNeta = listas[0][1] + listas[0][0]
            gananciaPersona = listas[0][2] * listas[1][2]
            return gananciaNeta * 100 - gananciaPersona
    elif apuestas == 2:
        if difGoles == 0:
            gananciaNeta = listas[0][1]
            gananciaPersona = listas[0][0] * listas[1][0]
            return gananciaNeta * 100 - gananciaPersona
        elif difGoles == 1:
            gananciaNeta = listas[0][0]
            gananciaPersona = listas[0][1] * listas[1][1]
            return gananciaNeta * 100 - gananciaPersona
    else:
        return listas[0] * listas[1] * -1


apuestas = int(input())
listas = list()
if apuestas == 3:
    em, vicgol, vicgol2 = map(int, input().strip().split())
    listas.append((em, vicgol, vicgol2))
    ga, gagol, gagol2 = map(int, input().strip().split())
    listas.append((ga, gagol, gagol2))
elif apuestas == 2:
    em, vicgol = map(int, input().strip().split())
    listas.append((em, vicgol))
    ga, gagol = map(int, input().strip().split())
    listas.append((ga, gagol))
else:
    em = int(input())
    listas.append(em)
    ga = int(input())
    listas.append(ga)

difGoles = int(input())

resultado = apu(listas, apuestas, difGoles)
print(resultado)
