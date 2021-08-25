#import numpy

def lecturaDeCasos(cad,lon):
    total=0.0
    for i in cad:
        if int(i)!= 0:
            total=total+float(i)
        elif int(i)==0:
            total=total+9.0
            lon=lon-1
    
    resto=total%lon
    if resto==0:
        total=total//lon
        total=round(total)
    else:
        total=total/lon
        total=round(total,5)
        
    return total
    

casos=int(input())
listaCasos=list()
for i in range(casos):
    cadena=input()
    listaCasos.append(cadena)

for i in listaCasos:
    lon=len(i)
    resultado=lecturaDeCasos(i,lon)
    print(resultado)
