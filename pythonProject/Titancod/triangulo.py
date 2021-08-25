

casos=int(input())
listaCasos=list()
for i in range(casos):
    x,y,z=map(int,input().strip().split())
    listaCasos.append((x,y,z))

for i in listaCasos:
    total= i[0]+i[1]+i[2]
    if total % 4==0:
        lado=total//4
        area=lado*lado
        print("L:"+str(lado)+" A:"+str(area))
    else:
        print("-1")
