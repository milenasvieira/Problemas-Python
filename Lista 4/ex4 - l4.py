rep = 1
grenais = 0
inter = 0
gremio = 0
empate = 0

while rep == 1:
    i, g = input() .split()
    i, g = int(i), int (g)
    
    grenais = grenais + 1
    
    if i > g:
        inter += 1
    elif g > i:
        gremio += 1
    elif i == g:
        empate += 1
    print("Novo grenal (1-sim 2-nao)")
    rep = int(input())
    if rep < 1 or rep > 2:
        rep = int(input())
    
print ("{} grenais" .format (grenais))
print ("Inter:{}" .format(inter))
print ("Gremio:{}" .format(gremio))
print ("Empates:{}" .format(empate))

if (inter > gremio):
    print ("Inter venceu mais")
elif (inter < gremio):
    print ("Gremio venceu mais")
else:
    print ("Nao houve vencedor")
    