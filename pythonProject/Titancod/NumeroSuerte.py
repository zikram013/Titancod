numero = int(input())
listaNumeros = list()
for i in range(0, numero):
    listaNumeros.append(i)

filtrado = list(filter(lambda x: x % 2 != 0, listaNumeros))
i = 1
while i != len(filtrado):
    n = filtrado[i]
    print(n)
    filtrado = list(filter(lambda x: listaNumeros.index(x) % n != 0, filtrado))
    print(filtrado)

    i+=1

print(filtrado)
print(len(filtrado))
