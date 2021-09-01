def ganancias(monto,apuestas):
    contador=monto
    listaApuestas=list()
    #contador-=1
    listaApuestas.append(1)
    for i in apuestas:
        if i=="W":
            contador-=listaApuestas[len(listaApuestas)-1]
            contador+=listaApuestas[len(listaApuestas)-1]
            contador+=listaApuestas[len(listaApuestas)-1]
            listaApuestas.append(1)
        else:
            ultimaApuesta=listaApuestas[len(listaApuestas)-1]
            if contador-ultimaApuesta>0:
                contador-=ultimaApuesta
                if ultimaApuesta!=1:
                    #contador-= ultimaApuesta*2
                    listaApuestas.append(ultimaApuesta*2)
                else:
                    #contador-=2
                    listaApuestas.append(2)
            else:
                return contador
        #print(contador)
    
    return contador

monto,apuestas=map(str,input().strip().split())
monto=int(monto)
resultado=ganancias(monto,apuestas)
print(resultado)
