def escalera(listaCajas):
    contador=0
    maxEscalera=len(listaCajas)
    
    for i in range(1,maxEscalera+1):
        print(contador)
        if int(listaCajas[i-1])>i:
            contador+=int(listaCajas[i-1])-i
        elif int(listaCajas[i-1])<i:
            contador+=int(listaCajas[i-1])-i
        else:
            contador=contador
    
    return contador

casos=int(input())
for i in range(casos):
    cajas=input().split(" ")
    listaCajasV=list(cajas)
    listaCajas=listaCajasV.pop(-1)
    resultado=escalera(listaCajas)
    print(resultado)
