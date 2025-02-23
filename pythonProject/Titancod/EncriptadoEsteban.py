"""
vocales -> espacios vacios
se guarda la vocal en orden y luego susituye en el mismo orden
se elimina la vocal
se termina la oracion y pone punto
si quedan vocales se ponen los ascii de esas vocales separados por un espacion cada uno
si en la lista hay menos vocales que espacios, se agrega un _
si la oracion inicia con vocal, se pone un _
"""

casos = 100

def encriptado(oracion):
    vocales = ['a', 'e', 'i', 'o', 'u']
    listaVocales = []
    iteracion = 0
    listaOracion = list(oracion)
    listaOracionV2 =[]
    for letra in listaOracion:
        if iteracion == 0 and vocales.__contains__(letra.lower()):
            listaVocales.append(letra)
            listaOracionV2.append("_")
            iteracion = iteracion + 1
        elif iteracion == len(listaOracion)-1:
            listaOracionV2.append(".")
        else:
            if letra == " ":
                if(len(listaVocales)==0):
                    listaVocales.append("_")
                else:
                    "listaOracionV2[iteracion] = listaVocales.pop(0)"
                    listaOracionV2.append(listaVocales.pop(0))
            elif letra in vocales:
                listaOracionV2.append(" ")
                listaVocales.append(letra)
            else:
                listaOracionV2.append(letra)

    if len(listaVocales)>0:
        for letra in listaVocales:
            listaOracionV2.append(str(int.from_bytes(letra.encode(),byteorder='big')))
            listaOracionV2.append(" ")

    cadena = "".join(listaOracionV2)

    return cadena


for i in range(casos):
    oracion = input().strip()
    if not oracion:
        break
    else:
        encrypt = encriptado(oracion)
        print(encrypt)