bolivia = "BOLIBIA"
casos = int(input())
listaCasos = list()
for i in range(casos):
    caso = input()
    listaCasos.append(caso)

for i in listaCasos:
    filterLetters=list(filter(lambda x:x in i,bolivia))
    if len(filterLetters) == len(bolivia):
        print("ES POSIBLE")
    else:
        print("NO ES POSIBLE")

"""
3
BOLIVIA
BOOIILVA
BOLVZATY
"""