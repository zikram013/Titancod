def dias(tiempo,meses):
    l=tiempo.split("/")
    diasanyoo=0
    contadorDias=int(l[0])
    #print(contadorDias)
    if(int(l[2])%4==0):
        contadorDias=contadorDias+1
        #print(contadorDias)
        diasanyoo=366
    else:
        diasanyoo=365
    mes=int(l[1])
    i=0
    while mes-1!=i:
        #print(meses[i])
        contadorDias=contadorDias+meses[i]
        i+=1
    #print(contadorDias)   
    return contadorDias,diasanyoo

def funcion(numerador, denominador):

    r_num = float(numerador)/funcion.divisor
    r_den = float(denominador)/funcion.divisor
    

    if(r_num.is_integer() and r_den.is_integer()):
        funcion(r_num,r_den)
    else:        
        if(funcion.divisor == numerador or funcion.divisor == denominador or r_num <= 1 or r_den <= 1):
            if numerador != denominador:
                print(str(int(numerador))+"/"+str(int(denominador))) 
            else:
                print("1")
        else:
            funcion.divisor += 1
            funcion(numerador, denominador)


diccionarioMes={
    "Ene":31,
    "Feb":28,
    "Mar":31,
    "Abr":30,
    "May":31,
    "Jun":30,
    "Jul":31,
    "Ago":31,
    "Sep":30,
    "Oct":31,
    "Nov":30,
    "Dic":31
}

listaDiasMes=[31,28,31,30,31,30,31,31,30,31,30,31]

casos=int(input())
listaFechas=list()
for i in range(casos):
    fecha=input()
    listaFechas.append(fecha)
    
#print(listaFechas)

for i in listaFechas:
    i=i.replace(' ','/')
    reDias,reAnyo=dias(i,listaDiasMes)
    #print(reDias," ", reAnyo)
    
    funcion.divisor=2
    funcion(reDias,reAnyo)
    
    
    
