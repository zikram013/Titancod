from math import factorial

def factorials(numero):
    nl=str(numero)
    tam=len(nl)
    contador=0
    for i in range(1,tam+1):
        digit=int(nl[i-1])
        sumas=factorial(tam+1-i)
        #print(sumas)
        contador+=sumas*digit
    
    return contador 
      
casos=None
while casos!=0:
    casos=int(input())
    if casos!=0:
        resultado=factorials(casos)
        print(resultado)
