def conversion(verso,vocales,caracter):
    for letra in verso:
        if letra in vocales:
            verso = verso.replace(letra,caracter)
    return verso

frases = int(input())
vocales = "aeiouAEIOU"
caracter = "-"
for i in range(frases):
    verso = input()
    resultado=conversion(verso,vocales,caracter)
    print(resultado)
