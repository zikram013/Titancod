def esPrimo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True


def teorema(x, y, z):
    total = 0
    i = 0
    m = 0

    while i < z:
        total = x + y * m
        if esPrimo(total):
            i += 1
        m += 1

    return total


x, y, z = map(int, input().strip().split())
# La secuencia que comienza en a se incrementa en b
total = 0
i = 0
valor = teorema(x, y, z)
print(valor)

"""
0-2
1-5
2-8
3-11
4-14
5-17
"""
