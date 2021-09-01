def mp(numero):
    contador=1
    multiplo=numero
    if numero==9:
        multiplo=numero*12345679
    else:
        while len(str(multiplo))!=str(multiplo).count("1")+str(multiplo).count("0"):
            multiplo=numero*contador
            contador+=1
    return multiplo

casos=None
while casos!=0:
    casos=int(input())
    if casos!=0:
        resultado=mp(casos)
        print(resultado)
