"""
6
3 2 3
2 8 5
2 4 10
4 4 1000
1 1 1
10 10 9
"""

def mod_pow(a, b, m):
    result = 1
    a %= m
    while b:
        if b & 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

t = int(input())
for _ in range(t):
    a, b, m = map(int, input().split())
    print(mod_pow(a, b, m))
