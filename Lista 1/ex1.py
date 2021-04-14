A, B, C = float (input().split())

if (A<B=C and B<A+C and C<A+B):
    perimetro = A+B+C
    print ("Perimetro = {:.1f}" .format(perimetro))
else:
    area = (C*(A+B))/2
    print ("Area = {:.1f}" .format(area))

