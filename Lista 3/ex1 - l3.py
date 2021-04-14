v1 = input()
v2 = input()
v3 = input()
v4 = input()
v5 = input()
v6 = input()
v1, v2, v3, v4, v5, v6 = float(v1), float(v2), float(v3), float(v4), float(v5), float(v6)

contador = 0
total = 0

valores = [v1, v2, v3, v4, v5, v6]
for i in valores:
     if i > 0:
         total += i
         contador += 1
         
print ("{} valores positivos" .format (contador))
print ("{:.1f}" .format (total/contador))