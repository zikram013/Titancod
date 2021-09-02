def sucesion(numero):
    sucList=list()
    sucList.append(0)
    contador=0
    act=0
    if numero==0:
        return 2
    else:
        while act<numero:
            if contador==0:
                act=2
            else:
                act=act+pow(3,contador-1)
                
            contador+=1
        return act+pow(3,contador-1)



#listaSucesion(2,3,6,15,42)

#S₁ = 2 + 0
#S₂ = 2 + 3⁰ = 3
#S₃ = 3 + 3¹ = 6
#S₄ = 6 + 3² = 15
#S₅ = 15 + 3³ = 42
#S₆ = 42 + 3⁴ = 123

numero=int(input())
resultado=sucesion(numero)
print(resultado)
