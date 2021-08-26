import string

def resolver(conversion,hexa):
    conversion1="".join(conversion)
    if len(conversion1)<8:
        return "MAL"
    else:
        if all(c in hexa for c in conversion1):
           return "BIEN"
        else:
            return "MAL"

casos=int(input())
listaCasos=list()
hexa="0123456789abcdefABCDEF"
for i in range(casos):
    cadena=input().strip().split("-")
    listaCasos.append((cadena))

for i in listaCasos:
    resultado=resolver(i,hexa)
    print(resultado)
