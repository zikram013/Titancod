casos=int(input())
procesar=int(input())
cadena=input()
cadena=list(cadena)
listaSinVacios=list()
listaErrados=list()
for i in cadena:
    if i != ' ':
        listaSinVacios.append(int(i))
        

for i in listaSinVacios:
    if i*2 %3 ==0:
        listaErrados.append(i*2)

#print(listaErrados)
print("La suma es "+str(sum(listaErrados)))
#print("La suma es",sum(listaSinVacios))
