import numpy as np


def erastotenes(x,y):
    numeros = list(range(2, x + 1))
    d = 0
    while numeros[d] ** 2 <= x:

        for n in numeros:
            if n != numeros[d]:
                if n % numeros[d] == 0:
                    numeros.remove(n)
        d += 1
    return numeros


def criba(n):
    primes = []
    isPrime = [1 for i in range(n)]
    isPrime[0] = isPrime[1] = 0

    for i in range(n):
        if isPrime[i]:
            primes.append(i)
            h = 2
            while i * h < n:
                isPrime[i * h] = 0
                h += 1

    return primes


casos = int(input())
for i in range(casos):
    x, y = map(int, input().strip().split())

    solucion = erastotenes(x,y)
    print(solucion)
