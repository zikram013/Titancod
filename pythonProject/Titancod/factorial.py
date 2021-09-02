def factorial(numero):
    nl=str(numero)
    tam=len(nl)
    contador=0
    for i in range(1,tam+1):
        digit=int(nl[i-1])
        sumas=0
        for j in range(1,tam+2-i):
            #print("entra")
            sumas+=digit*j
            #print(sumas)
        contador+=sumas
    
    return contador 
      
casos=None
while casos!=0:
    casos=int(input())
    if casos!=0:
        resultado=factorial(casos)
        print(resultado)
