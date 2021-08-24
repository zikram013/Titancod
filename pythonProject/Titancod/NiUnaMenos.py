def comprobacion(palabraTotal,alfalist,alfa):
    listPalabraTotal=list(palabraTotal)
    faltan=""
    filterLetters = list(filter(lambda x: x not in listPalabraTotal,alfalist))
    if len(filterLetters)==0:
        return "OK"
    else:
        for ele in filterLetters:
            faltan+=ele
        return faltan 
    
    

alfa = "abcdefghijklmnopqrstuvwxyz"
alfalist=list(alfa)
prueba=int(input())
palabras=list()
for i in range(prueba):
    palabras.append([])

for i in range(prueba):
    pal=int(input())
    for j in range(pal):
        p=input()
        palabras[i].append(p)

for i in palabras:
    palabraTotal="".join(i)
    resultado=comprobacion(palabraTotal,alfalist,alfa)
    print(resultado)
