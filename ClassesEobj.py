class Casa():
    def __init__(self, rua, bairro, cep, numero):
        self.rua = rua
        self.bairro = bairro
        self.cep  = cep
        self.numero = numero
    
    def enderecoCompleto(self):
        return "Endereço completo: " +  self.rua + ", " + self.bairro + ", " + self.cep + ", " + self.numero

casa1 = Casa(rua = "Rua Ceara", bairro = "Jardim dos Estados", cep = "3", numero = "0")
casa2 = Casa(rua = "Rua Urubu do Pix", bairro = "Jorge dos Mundos", cep = "20quatro", numero = "b")
casa3 = Casa(rua = "Matuêpeixe", bairro = "Shaolin Matador de Porco", cep = "Juju do Pix", numero = "404")
























