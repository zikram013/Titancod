def expresion(caso):
    
    if caso==0:
        return "1"
    elif caso==1:
        return "1 1 1"
    else:
        cadena="1"
        coef=2*caso
        coef+=1
        contador=2
        #print(coef)
        m=coef/2
        m+=1
        for i in range(2,coef+1):
            if m>=i:
                cadena+=" "+ str(i)
            else:
                t=len(cadena)
                ind=int(cadena[t-1])
                cadena+=" "+str(ind-1)
                #contador+=2
        return cadena

casos=int(input())
for i in range(casos):
    cas=int(input())
    resultado=expresion(cas)
    print(resultado)
