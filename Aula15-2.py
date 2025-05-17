def quadrado_cubo():
    try:
        n = int(input("Digite o número entre 2 e 999: "))
        if n <= 1 or n >= 1000:
            print ("Muito pequeno ou grande.")
        else:
            for i in range(1, n+1):
                print (i, i**2, i**3)
    except ValueError:
        print("ERRO!")            


quadrado_cubo()








































