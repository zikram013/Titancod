"""
4
-4 -5 8 0 -5 -3
-4 -4 3 3 -5 -3
-4 -3 8 7 -5 -2
-4 -2 5 7 -5 -1
"""
def Comprobacion(x1, y1, x2, y2, x3, y3):
    a2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    b2 = (x3 - x2) ** 2 + (y3 - y2) ** 2
    c2 = (x3 - x1) ** 2 + (y3 - y1) ** 2

    return a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2

casos = int(input())

for i in range(casos):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    if Comprobacion(x1, y1, x2, y2, x3, y3):
        print("SI")
    else:
        print("NO")
