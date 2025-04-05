# Fazer classe chamada ANIMAL, colocar no init self, o nome e a idade do animal

class Animal():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 100
    def dormir(self, horas):
        energiaGanha = horas * 10
        self.energia = self.energia + energiaGanha
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nome} dormiu por {horas} e ganhou {energiaGanha}, totalizano em {self.energia}")
    def brincar(self, tempobrincando):
        energiaGasta = tempobrincando * 5
        if self.energia >= energiaGasta:
            self.energia -= energiaGasta
            print(f"{self.nome} brincou por {tempobrincando} e gastou {energiaGasta}. Sua energia atual agora é {self.energia}")
        else:
            print(f"{self.nome} está cansado demais para brincar!")


animal1 = Animal(nome = ("Quiuí", "))
animal1.brincar(tempobrincado = 10)
animal1.dormir(horas = 4)


























