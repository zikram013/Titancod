def esPrimo(digito):
    for n in range(2,digito):
        if digito%n==0:
            return False
    return True

def primos(num):
    listaPrimos=list()
    for i in num:
        if i!="":
            if esPrimo(int(i)):
                listaPrimos.append(int(i))
                #if len(listaPrimos)==3:
                    #break
    return listaPrimos
    
def pintar(lista):
    lista.sort()
    #print(lista)
    if len(lista)==1:
        print(str(lista[0])+", -1, -1")
    elif len(lista)==2:
        print(str(lista[0])+", "+str(lista[1])+", -1")
    elif len(lista)>2:
        print(str(lista[0])+", "+str(lista[1])+", "+str(lista[2]))
    else:
        print("-1,","-1,","-1,")
        

casos=int(input())

for i in range(casos):
    cantidad=int(input())
    numeros=input().strip().split()
    resultado=primos(numeros)
    #print(resultado)
    pintar(resultado)
    
