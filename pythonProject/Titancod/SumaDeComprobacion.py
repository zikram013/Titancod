def buscarPosicion(letra, abcedario):
    posicion = abcedario.index(letra)
    return posicion


frase = input()
fraseM = frase.upper()
total = 0
alfa = "abcdefghijklmnopqrstuvwxyz"
alfaM = alfa.upper()
alfaList = list(alfaM)
for i in range(1, len(fraseM)+1):
    if fraseM[i - 1] == " ":
        total = total + 0
    else:
        pos = buscarPosicion(fraseM[i - 1], alfaList)
        total = total + pos * i

print(total)
