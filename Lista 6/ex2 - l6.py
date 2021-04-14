N = 0
T = int (input())

while T >= 2 and T <= 50:
        for i in range (0,1000):
            print ("N[{}] = {}" .format(i, N))
            N += 1
            if N == T:
                N = 0