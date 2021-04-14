risada = input()
risadaInversa = 0

for letras in risada:
    if letras != "a" and letras != "e" and letras != "i" and letras != "o" and letras != "u":
        risada = risada.replace(letras,"")

risadaInversa = risada[::-1]

if risadaInversa == risada:
    print ('S')
else:
    print ('N')
    