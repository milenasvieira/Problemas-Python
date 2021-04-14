lista = []

for i in range(20):
    N = int (input())
    lista.append(N)

listaTrocada = lista[::-1]

for j in range(20):
    print ("N[{}] = {}" .format(j, listaTrocada[j]))

