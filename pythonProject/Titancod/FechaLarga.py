"""
4
<--->--==>
<<<<<<<<<<
----==-
<----=====>
"""

def Flecha(entrada):
    maxLarga = -1
    entrada = list(entrada)
    i = 0

    while i < len(entrada):
        if entrada[i] =='<':
            j = i+1
            while j < len(entrada) and entrada[j] in '-':
                j+=1
            maxLarga = max(maxLarga, j-i)

        if entrada[i] =='<':
            j = i+1
            while j < len(entrada) and entrada[j] in '=':
                j+=1
            maxLarga = max(maxLarga, j-i)

        if entrada[i] == '-':
            j = i
            while j < len(entrada) and entrada[j] == '-':
                j += 1
            if j < len(entrada) and entrada[j] == '>':
                maxLarga = max(maxLarga, j - i + 1)

        if entrada[i] == '=':
            j = i
            while j < len(entrada) and entrada[j] == '=':
                j += 1
            if j < len(entrada) and entrada[j] == '>':
                maxLarga = max(maxLarga, j - i + 1)
        i+=1

    return maxLarga

casos = int(input())
for i in range(casos):
    entrada = input().strip()
    resultado = Flecha(entrada)
    print(resultado)
