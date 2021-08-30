def descodificar(cod):
    codli=list()
    c=list(cod)
    for i in range(len(cod)-1):
       if cod[i]=="p" and cod[i-1]==cod[i+1]:
        codli.append(i)
        codli.append(i+1)
    j=0    
    for i in codli:
        c.pop(int(i)-j)
        j+=1
        
    desco=''.join(str(e)for e in c)
    return desco

casos=int(input())
for i in range(casos):
    cod=input()
    resultado=descodificar(cod)
    print(resultado)
