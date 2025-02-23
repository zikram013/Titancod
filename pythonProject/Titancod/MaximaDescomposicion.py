import sys


def main():
    # Leer toda la entrada de una sola vez
    data = sys.stdin.read().strip().split()
    if not data:
        return
    T = int(data[0])
    index = 1
    results = []

    for _ in range(T):
        N = int(data[index])
        index += 1
        found = False

        # Determinar el máximo valor de L tal que L*(L+1)/2 <= N
        maxL = 1
        L = 2
        while L * (L + 1) // 2 <= N:
            maxL = L
            L += 1

        # Buscar la secuencia de mayor longitud (de maxL a 2)
        for L in range(maxL, 1, -1):
            numerator = N - (L * (L - 1) // 2)
            if numerator % L == 0:
                a = numerator // L
                if a > 0:
                    # Se encontró la secuencia: desde a hasta a+L-1
                    results.append(" ".join(str(a + i) for i in range(L)))
                    found = True
                    break

        if not found:
            results.append("-1")

    sys.stdout.write("\n".join(results))


if __name__ == '__main__':
    main()
