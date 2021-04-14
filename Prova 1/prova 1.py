ate15 = 0 
ate30 = 0
ate45 = 0
ate60 = 0
acima60 = 0
idade = -1

while idade != 0:
    idade = int (input())
    if idade > 0:
        if idade <= 15:
            ate15 += 1
        elif idade <= 30:
            ate30 += 1
        elif idade <= 45:
            ate45 += 1
        elif idade <= 60:
            ate60 += 1
        elif idade > 60:
            acima60 += 1

print (ate15)
print (ate30) 
print (ate45) 
print (ate60) 
print (acima60)
print ("{:.1f}" .format (((ate60+acima60)/(ate15+ate30+ate45+ate60+acima60))*100))