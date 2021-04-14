nota_invalida = True

while nota_invalida:
    nota1 = float(input())
    if nota1 >= 0 and nota1 <= 10:
        nota_invalida = False
    else:
        print ("nota invalida")

nota_invalida = True

while nota_invalida:
    nota2 = float(input())
    if nota2 >= 0 and nota2 <= 10:
        nota_invalida = False
    else:
        print ("nota invalida")

print ("media = {:.2f}" .format((nota1+nota2)/2))