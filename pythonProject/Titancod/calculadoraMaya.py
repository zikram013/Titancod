def sumatorio(cincos,tres,dos,uno):
    contador=0
    rep=cincos.count("1")
    contador+=5*rep
    rep=tres.count("1")
    contador+=3*rep
    rep=dos.count("1")
    contador+=2*rep
    rep=uno.count("1")
    contador+=1*rep
    return contador

casos=int(input())

for i in range(casos):
    cadena=input()
    cincos=cadena[0:5]
    tres=cadena[5:8]
    dos=cadena[8:10]
    uno=cadena[10:11]
    resultado=sumatorio(cincos,tres,dos,uno)
    print(resultado)
