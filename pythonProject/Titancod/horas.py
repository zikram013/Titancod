tiempo=input()
lon=len(tiempo)
puntos=tiempo.index(":")
hora=tiempo[0:puntos]
minuto=tiempo[puntos+1:lon]
horaTotal=int(hora)*60+int(minuto)

sumarTiempo=input()
if sumarTiempo.contains(":"):
    lon=len(sumarTiempo)
    puntos=sumarTiempo.index(":")
    hora=tiempo[0:puntos]
    minuto=tiempo[puntos+1:lon]
    horaTotalSum=int(hora)*60+int(minuto)
    horaTotal+=horaTotalSum
    
    print(horaTotal)
else:
    if sumarTiempo>60:
        sumarTiempo=sumarTiempo/60
    
    
