I = 1
J = 60

while J >= 0:
    for i in range (0,J):
        if I >= 0 and J >= 0:
            print('I={} J={}'.format(I, J))
            J = J - 5
            I = I + 3
    