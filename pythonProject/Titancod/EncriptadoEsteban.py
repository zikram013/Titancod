def encriptado(oracion):
    vocales = "aeiouAEIOU"
    listaVocales = []
    listaOracionV2 = []
    iteracion = 0
    
    for letra in oracion:
        if iteracion == 0 and letra in vocales:
            listaVocales.append(letra)
            listaOracionV2.append("_")
        elif letra in vocales:
            listaOracionV2.append(" ")
            listaVocales.append(letra)
        elif letra == " ":
            if listaVocales:
                listaOracionV2.append(listaVocales.pop(0))
            else:
                listaOracionV2.append("_")
        else:
            listaOracionV2.append(letra)
        iteracion += 1
    
    listaOracionV2.append(".")
    
    if listaVocales:
        listaOracionV2.append(" ")
        listaOracionV2.append(" ".join(str(ord(v)) for v in listaVocales))
    
    return "".join(listaOracionV2)

def main():
    casos = 100
    for _ in range(casos):
        oracion = input().strip()
        if oracion:
            print(encriptado(oracion))
        else:
            break

if __name__ == "__main__":
    main()
