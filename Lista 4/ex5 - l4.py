nota_valida = 0
novo_calculo = 0
soma = 0
X = 0

while novo_calculo != 2:
    X = float(input())

    if X >= 0 and X <= 10:
        soma += X
        nota_valida += 1
    else:
        print ("nota invalida")

    if nota_valida == 2:
        print ("media = {:.2f}" .format (soma/2))
        soma = 0
        nota_valida = 0
        X = 0
        print("novo calculo (1-sim 2-nao)")
        novo_calculo = int(input())

        while novo_calculo != 2 and novo_calculo != 1:
            print("novo calculo (1-sim 2-nao)")
            novo_calculo = int(input())

