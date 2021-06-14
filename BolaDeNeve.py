'''Pcotas = float(input("DIGITE PREÇO DA COTA"))
Vdividendos = float(input("DIGITE O DIVENDO POR COTA"))
Qcotas = float(input("DIGITE A QUANTIDADE DE COTAS ATUAL"))

quantidade = float(input("DIGITE A QUANTIDADE DE COTAS ATUAL"))
meses = float(input("DIGITE A QUANTIDADE DE MESES"))'''

carteira = 0

Pcotas = 10.61
Vdividendos = 0.07
Qcotas = 9091

meses = 480

tempo = 0

while meses != tempo:
    Tdividendos = Vdividendos * Qcotas
    print("~~~~~~~~~~~~~~ {}° mês ~~~~~~~~~~~~~~~~~~".format(tempo))
    print("DIVIDENDOS GERADOS:", Tdividendos)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if carteira > Pcotas:
        Mcomprar = int( carteira / Pcotas)
        carteira = carteira - (Mcomprar * Pcotas)
        Qcotas = Qcotas + Mcomprar
        print("~~~~~~~~~~~~~~ {}° mês ~~~~~~~~~~~~~~~~~~".format(tempo))
        print("QUANTIDADE GERADAS DE COTAS:",Qcotas)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
    else:
        carteira = Tdividendos + carteira
        print("~~~~~~~~~~~~~~ {}° mês ~~~~~~~~~~~~~~~~~~".format(tempo))
        print("VALOR QUE SOBROU PARA A CARTEIRA", carteira)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    tempo = tempo +1
    

