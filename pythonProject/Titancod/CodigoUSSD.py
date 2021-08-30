def comprobar(ussd):
    if ussd[0]!="*":
        return "mal"
    elif ussd[4]!="*":
        return "mal"
    else:
        primeraParte=ussd[1:4]
        #print(primeraParte)
        if primeraParte.isdigit():
            if ussd[len(ussd)-1]=="#":
                segundaParte=ussd[5:len(ussd)-1]
                #print(segundaParte)
                if segundaParte.isdigit():
                    return"bien"
                else:
                    return "mal"
            else:
                return "mal"
        else:
            return "mal"
        


casos=int(input())
for i in range(casos):
    ussd=input()
    resultado=comprobar(ussd)
    print(resultado)
