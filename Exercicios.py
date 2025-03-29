salario = float(input())
if (salario <= 400.00 and salario >= 0):
    novosalario = salario * 1.15
    reajuste = novosalario - salario
    percentual = 15
    print ("Novo salario: %.2f" %novosalario)
    print ("Reajuste ganho : %.2f" %reajuste)
    print ("Percentual:", percentual, "%")
elif (salario <= 400.01 and salario >= 800.00):
    novosalario = salario * 1.12
    reajuste = novosalario - salario
    percentual = 12
    print ("Novo salario: %.2f" %novosalario)
    print ("Reajuste ganho : %.2f" %reajuste)
    print ("Percentual:", percentual, "%")
elif (salario <= 800.01 and salario >= 1200.00):
    novosalario = salario * 1.10
    reajuste = novosalario - salario
    percentual = 10
    print ("Novo salario: %.2f" %novosalario)
    print ("Reajuste ganho : %.2f" %reajuste)
    print ("Percentual:", percentual, "%")
elif (salario <= 1200.01 and salario >= 2000.00):
    novosalario = salario * 1.07
    reajuste = novosalario - salario
    percentual = 7
    print ("Novo salario: %.2f" %novosalario)
    print ("Reajuste ganho : %.2f" %reajuste)
    print ("Percentual:", percentual, "%")
elif (salario > 2000.00):
    novosalario = salario * 1.04
    reajuste = novosalario - salario
    percentual = 4
    print ("Novo salario: %.2f" %novosalario)
    print ("Reajuste ganho : %.2f" %reajuste)
    print ("Percentual:", percentual, "%")

















