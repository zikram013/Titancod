def contarDados(tiradas):
    total=0
    contadorRe=1
    listP=list()
    listP.append(sum(tiradas[0]))
    listP.append(sum(tiradas[1]))
    listP.append(sum(tiradas[2]))
    for i in listP:
        if i>total and i%2==0:
            total=i
        elif i==total and i%2==0:
            contadorRe+=1
    
    if total==0:
        return "Nadie"
    elif contadorRe<3:
        pos=listP.index(total)
        if pos==0:
            return "Hugo"
        elif pos==1:
            return "Paco"
        else:
            return "Luis"
    else:
        return "NADIE"
    

diccionarioCasos=dict()
casos=int(input())
player=3
for i in range(casos):
    diccionarioCasos[i] = []

for i in range(casos):
    for j in range(player):
        tirada1,tirada2=map(int,input().strip().split())
       
        diccionarioCasos[i].append((tirada1,tirada2))


for i in diccionarioCasos:
    v=diccionarioCasos.get(i)
    resultado=contarDados(v)
    print(resultado)
