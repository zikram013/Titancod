def escalera(listaCajas):
    contador=0
    maxEscalera=len(listaCajas)
    #print(listaCajas)
    for i in range(1,maxEscalera+1):
        print(i)
        print(listaCajas[i-1])
        if int(listaCajas[i-1])>i:
            contador+=int(listaCajas[i-1])-i
            print(contador)
        elif int(listaCajas[i-1])<i:
            contador-=i-int(listaCajas[i-1])
            print(contador)
        else:
            contador=contador
            print(contador)
    
    return contador

casos=int(input())
for i in range(casos):
    cajas=input().split(" ")
    listaCajasV=list(cajas)
    #print(listaCajasV)
    resultado=escalera(listaCajasV)
    print(resultado)
