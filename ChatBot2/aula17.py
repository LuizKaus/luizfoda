import random

def saudacoes(nome):
    frases = ["Bom dia! Meu nome é " + nome + ". Como vai você?", "Olá!", "Oi, tudo bem?"]
    print(frases[random.randint(0,2)])


def receba():
    texto = "Cliente: " + input("Cliente: ")
    palavra_proibida = ["Bocó", "bocó", "Zé ruela", "Ordinário",]
    for i in palavra_proibida:
        if i in texto:
            print("196.53.206.14")
    return texto

def busca_resposta(nome,texto):
    with open("BaseDeConhecimento.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("Cliente:", "") == "Tchau":
                    print(nome+ ": volte sempre!")
                    return "fim"
            elif viu.strip() == texto.strip():
                proxima_linha = conhecimento.readline()
                if "Chatbot: " in proxima_linha:
                    return proxima_linha
        else:
            print("Me desculpe! Não sei o que falar.")
            conhecimento.write("\n" + texto)
            resposta_user = input("O que esperava?\n")
            conhecimento.write("\n" + "Chatbot: " + resposta_user)
            return "Hum..."

busca_resposta("Cliente: ", "Você tem amigos?")





# saudacoes(input())
# receba()








