numero=int(input())
listaNumeros = list()
for i in range(1, numero+1):
    listaNumeros.append(i)

filtrado = list(filter(lambda x: x % 2 != 0, listaNumeros))
i = 1
while  len(filtrado) >i:
    
    n=filtrado[i]
    aux=filtrado[:n-1]
    aux2=filtrado[n-1:]
    aux2=list(filter(lambda x:aux2.index(x)%n!=0,aux2))
    filtrado=aux+aux2

    i+=1

print(len(filtrado))
