salario = float (input())

if (salario <= 400.00):
    reajuste = salario * 0.15
    novo_salario = salario + reajuste
    percentual = 15%
    print ("Novo salario: {:.2f}" .format(novo_salario))
    print ("Reajuste ganho: {:.2f}" .format(reajuste))
    print ("Em percentual: {}" .format(percentual))
elif (salario >= 400.01 and salario <= 800.00):
    reajuste = salario * 0.12
    novo_salario = salario + reajuste
    percentual = 12%
    print ("Novo salario: {:.2f}" .format(novo_salario))
    print ("Reajuste ganho: {:.2f}" .format(reajuste))
    print ("Em percentual: {}" .format(percentual))
elif (salario >= 800.01 and salario <= 1200.00):
    reajuste = salario * 0.10
    novo_salario = salario + reajuste
    percentual = 10%
    print ("Novo salario: {:.2f}" .format(novo_salario))
    print ("Reajuste ganho: {:.2f}" .format(reajuste))
    print ("Em percentual: {}" .format(percentual))
elif (salario >= 1200.01 and salario <= 2000.00):
    reajuste = salario * 0.07
    novo_salario = salario + reajuste
    percentual = 7%
    print ("Novo salario: {:.2f}" .format(novo_salario))
    print ("Reajuste ganho: {:.2f}" .format(reajuste))
    print ("Em percentual: {}" .format(percentual))
else:
    reajuste = salario * 0.04
    novo_salario = salario + reajuste
    percentual = 4%
    print ("Novo salario: {:.2f}" .format(novo_salario))
    print ("Reajuste ganho: {:.2f}" .format(reajuste))
    print ("Em percentual: {}" .format(percentual))