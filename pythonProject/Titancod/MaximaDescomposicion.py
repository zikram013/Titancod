def sumas(n, init):
    numerosSumados = list()
    mitad = (n // 2) + 1
    contador = 0
    for i in range(init, mitad + 1):
        contador = contador + i
        if contador <= n:
            numerosSumados.append(i)
            return numerosSumados
        else:
            numerosSumados = sumas(n, init + 1)
    return numerosSumados


casos = int(input())
listaCasos = list()
for i in range(casos):
    c = int(input())
    listaCasos.append(c)

for c in listaCasos:
    resultado = sumas(c, 1)
    if len(resultado) == 1:
        print(resultado[0])
    else:
        resultado = map(str, resultado)
        nums = " ".join(resultado)
        print(nums)




"""
4
5
8
23
90
"""
