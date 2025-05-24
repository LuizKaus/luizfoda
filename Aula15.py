# try:
#     num1 = int(input())
#     num2 = int(input())
#     soma = num1 + num2
# except ValueError:
#     print("Você DIGITOU ERRADO!!!!!!!!!!!!!!!!!!😡🤬😡👿👹👺")
# else:
#     print("O valor da soma é: ", soma)


def dividir_numeros():
    while True:
        try:
            num3 = float(input())
            num4 = float(input())
            divisao = num3 / num4
        except ValueError:
            print("Você SÓ DIGITA ERRADO CARA!! 👹👹👿☠☠☠")
        except ZeroDivisionError:
            print("Não da pra DIVIDIR POR ZERO CARA. 😔😔")
        else:
            print("O resultado da divisão é: ", divisao)
            break

def pergunta_numero():
    aux = 1
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
        except ValueError:
            print("mano '-'")
        else:
            print("O número inteiro digitado foi: ", numero)
            break
        finally:
            print("Tentativa de número", aux)
            aux = aux + 1






pergunta_numero()
# dividir_numeros()



























































































































































