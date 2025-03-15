import geometria as g

def menu():
    print("Calculadora Geométrica🥶🥶🥶")
    print("1 - Área do Círculo")
    print("2 - Perímetro do Círculo")
    print("3 - Área do Retângulo")
    print("4 - Perímetro do Retângulo")
    print("5 - Área do Triângulo")
    print("6 - Perímetro do Triângulo")
    print("7 - Área do Cubo")
    print("8 - Perímetro do Cubo")
    print("0 - Sair 🥸💀👺👹👽👻🦒")

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
      raio = float(input("Raio: "))
      print(f"Área: {g.areaCirculo(raio)}") 
    elif opcao == 2:
      raio = float(input("Raio: "))
      print (f"Perímetro: {g.perimetroCirculo(raio)}")
    elif opcao == 3:
      base = float(input("Base: "))
      altura = float(input("Altura: "))
      print (f"Área: {g.areaRetangulo(base, altura)}")
    elif opcao == 4:
       base = float(input("Base: "))
       altura = float(input("Altura: "))
       print (f"Perímetro: {g.perimetroRetangulo(base, altura)}")
    elif opcao == 5:
       base = float(input("Base: "))
       altura = float(input("Altura: "))
       print (f"Área: {g.areaTriangulo(base, altura)}")
    elif opcao == 6:
       lado1 = float(input("Lado 1:"))
       lado2 = float(input("Lado 2:"))
       lado3 = float(input("Lado 3:"))
       print (f"Perímetro: {g.perimetroTriangulo(lado1, lado2, lado3)}")
    elif opcao == 7:
        base = float(input("Base: "))
        print (f"Área: {g.areaCubo(base)}")
    elif opcao == 8:
       aresta = float(input("Aresta: "))
       print (f"Perímetro: {g.perimetroCubo(aresta)}")
    elif opcao == 0:
       print ("Saindo...")
       break
    else:
       print ("Esse comando não existe")
    





    















