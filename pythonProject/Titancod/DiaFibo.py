"""
11 23
2 13
6 11
8 13
"""

casos = 10000
def fibonacci_string(n):
    fib = [1, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return ''.join(str(x) for x in fib)

for i in range(casos):
    line = input().strip()
    if not line:
        break
    else:
        mes, dia = map(int, line.split())
        fibo = fibonacci_string(30)
        cadenaFecha = str(mes) + str(dia)
        if cadenaFecha in fibo:
            print("SI")
        else:
            print("NO")




