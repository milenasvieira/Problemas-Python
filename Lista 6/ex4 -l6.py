pares = []
impares = []

for i in range (15):
    valor = int (input())
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    if len (pares) == 5:
        posicaoPares = 0
        for j in pares:
            print ("par[{}] = {}" .format(posicaoPares, j))
            posicaoPares += 1
        pares = []

    if len (impares) == 5:
        posicaoImpares = 0
        for k in impares:
            print ("impar[{}] = {}" .format(posicaoImpares, k)
            posicaoImpares += 1
        impares = []

if len (impares) > 0:
    posicaoImpares = 0
    for k in impares:
        print ("impar[{}] = {}" .format(posicaoImpares, k)
        posicaoImpares += 1

if len (pares) > 0:
    posicaoPares = 0
    for j in pares:
        print ("par[{}] = {}" .format(posicaoPares, j))
        posicaoPares += 1