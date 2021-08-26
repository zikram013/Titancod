def esCapicua(numero):
    return numero == int(str(numero)[::-1])


def sumatorio(n):
    total = n
    contador = 0
    while not esCapicua(total) and contador != 100:
        aux = total
        inverso = int(str(aux)[::-1])
        total += inverso
        contador += 1
    return total


casos = int(input())
listaCasos = list()
for i in range(casos):
    numero = int(input())
    resultado = sumatorio(numero)
    print(resultado)
