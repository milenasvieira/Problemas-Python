X = float (input())
N = []

for i in range (100):
    N.append(X)
    print ("N[{}] = {:.4f}" .format(i, X))
    X = X/2
