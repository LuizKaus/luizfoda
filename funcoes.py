def soma(a,b,c):
    return a + b + c


def divisao(a,b):
    return a / b

def multiplicacao(a,b,c):
    return a * b * c


print (soma(5,3,4))
print (soma(4,2,5))
print(multiplicacao(5,4,2))
print (divisao(5,2))

def fimdesemana():
    print("FDS")

def menor(a,b):
    if a <= b:
        return a
    else:
        return b 

def maior(a,b):
    if a >= b:
        return a
    else:
        return b
    
print (menor(1,2))
print (maior(2,4))

def velMedia(distancia,tempo):
    return distancia / tempo

a = float(input("Digite a distancia: "))
b = float(input("Digite o tempo: "))

print (velMedia(a,b))






