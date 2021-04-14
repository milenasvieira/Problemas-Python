A, B, C = input() .split()
A, B, C = float (A), float (B), float (C)

if (A>B):
    A,B = B,A
elif (A>C):
    A,C = C,A
elif (B<C):
    B,C = C,B

if (A >= B+C):
    print ('NAO FORMA TRIANGULO')
elif (A**2 = B**2+C**2):
    print ('TRIANGULO RETANGULO')
elif (A**2 > B**2+C**2):
    print ('TRIANGULO OBTUSANGULO')
elif (A**2 < B**2+C**2):
    print ('TRIANGULO ACUTANGULO')
elif (A == B == C):
    print ('TRIANGULO EQUILATERO')
elif (A == B or A == C or B == C):
    print ('TRIANGULO ISOSCELES')