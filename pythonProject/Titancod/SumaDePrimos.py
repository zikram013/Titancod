def esPrimo(digito):
    for n in range(2,digito):
        if digito%n==0:
            return False
    return True

def primos(n):
    listaPrimos=list()
    for i in range(2,n):
        if esPrimo(i):
            listaPrimos.append(i)
            b=n-i
            for j in range(2,b):
                if esPrimo(j):
                    listaPrimos.append(j)
                    c=b-j
                    if esPrimo(c):
                        listaPrimos.append(c)
                        return listaPrimos
                    listaPrimos.remove(j)
        listaPrimos.remove(i)

casos=int(input())
for i in range(casos):
    numero=int(input())
    resultado=primos(numero)
    print(resultado[0],resultado[1],resultado[2])

"""
4
31
61
71
7
"""