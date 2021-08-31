import math

def verificacion(caso):
    contador=0
    for i in range(1,len(caso)+1):
        if i%2==0:
            contador+=3*int(caso[i-1])
        else:
            contador+=int(caso[i-1])
    #print(contador)
    red=(math.ceil(contador/10.0)*10)
    #print(red)
    return red-contador

casos=int(input())
for i in range(casos):
    cas=input()
    resultado=verificacion(cas)
    print(resultado)
