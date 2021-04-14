N = input()
N = int(N)
contador = 0
total = 0

for i in range (0,10000):
    if i % N == 2 and N < 10000:
        contador += 1
        total = i
        print ("{}" .format (total))
