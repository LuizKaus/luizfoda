class animal:
    def identificar(self, vertebras, classe, alimentacao):
        raise NotImplementedError("😎 erro")

class vertebrado(animal):
    mapa = {("ave" , "carnivoro"): "aguia",
            ("ave" , "onivoro"): "pomba",
            ("mamifero" , "onivoro"): "humano",
            ("mamifero" , "herbivoro"): "vaca"}
    def identificar(self, vertebras, classe, alimentacao):
        raise NotImplementedError("😎 erro")

class invertebrado(animal):
    mapa = {("inseto" , "hematofago"): "aguia",
            ("inseto" , "herbivoro"): "lagarta",
            ("anelideo" , "hematofago"): "sanguessuga",
            ("anelideo" , "onivoro"): "minhocas"}
    def identificar(self, vertebras, classe, alimentacao):
        raise NotImplementedError("😎 erro")

vertebra = input()
classe = input()
alimentacao = input()

if vertebra == "vertebrado":
    animal = vertebrado()
elif vertebra == "invertebrado":
    animal = invertebrado()

print(animal.identificar(vertebras, classe, alimentacao))

































