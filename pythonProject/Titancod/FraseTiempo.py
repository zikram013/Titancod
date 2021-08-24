  
from datetime import timedelta


# timeformat = [str(timedelta(seconds=0.34))]
# print(timeformat)
eliminarNoLetras = lambda str: "".join(re.findall("[\w]", str))


casosDePrueba = int(input())
listaEntradas = list()
alfa = "abcdefghijklmnopqrstuvwxyz"
alfalist = list(alfa)
pos = 0
listaSinVacios = list()
for i in range(casosDePrueba):
    xmin = input()

    xmax = input()

    text = input()
    xmax2 = str(timedelta(seconds=float(xmax)))
    xmin2 = str(timedelta(seconds=float(xmin)))
    listaEntradas.append((xmin2, xmax2, text))

for i in range(len(listaEntradas)):

    valor = listaEntradas[i][2]
    if valor != '""' or listaEntradas[i][2] != '""':
        listaSinVacios.append(listaEntradas[i])
        
todo = len(listaSinVacios)-1
j=0

prueba=(listaSinVacios[1][2])
new_string=prueba.replace('"','')


for i in listaSinVacios:
    print('0'+str(i[0])[:-4])
    print('0'+str(i[1])[:-4])
    og=str(i[2])
    og2=og.replace('"','')
    aux=str(eliminarNoLetras(og2))
    
    if og2==aux:
    	og3=og2.lower()
    	print(og3)
    else:
    	print(aux)
    
    if j!=todo:
    	print("")
    	j+=1
