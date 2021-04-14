textoCorreto = ""
texto = input() .split()

for i in texto:
    if len (i) >= 4:
        if i[0:1] == i[2:3]:
            i = i[2:]
    textoCorreto = textoCorreto + i + " "
textoCorreto = textoCorreto.strip()

print (textoCorreto)