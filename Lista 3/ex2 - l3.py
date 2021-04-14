v1 = input()
v2 = input()
v3 = input()
v4 = input()
v5 = input()

v1, v2, v3, v4, v5 = int(v1), int(v2), int(v3), int(v4), int(v5)

contador = 0
v = [v1, v2, v3, v4, v5]

for i in v:
    if i % 2 == 0:
        contador += 1
print ("{} valores pares" .format (contador))