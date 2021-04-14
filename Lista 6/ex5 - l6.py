N = int (input())
X = []

for i in range (0, N):
    valores = input()
    valores = valores.strip()
    X.append(valores)
    
    for j in range(len (X)):
        X[j] = int (X[j])
        
        posicao = 0
        menor = X[0]
        contador = 0

        for j in X:
            if j < menor:
                menor = j
                posicao = contador
            contador += 1

print ("Menor valor: {}" .format(menor))
print ("Posicao: {}" .format(posicao))
