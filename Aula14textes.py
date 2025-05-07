import unittest

def sobrenomeNaOrdem(nome, sobrenome1, sobrenome2):
    if(len(sobrenome1) > len(sobrenome2)):
        return nome+" "+ sobrenome1+" "+ sobrenome2
    else:
         return nome+" "+ sobrenome2+" "+ sobrenome1

  
    
class NomeTest(unittest.TestCase):
    def test_sobrenomeNaOrdem(self):
        nomeCompleto = sobrenomeNaOrdem("Luiz Henrique", "von Holleben", "Kaus")
        self.assertEqual(nomeCompleto, "Luiz Henrique von Holleben Kaus")
    def test_sobrenomeNaOrdem2(self):
        nomeCompleto2 = sobrenomeNaOrdem("Peer", "Werner Kaus", "Maximilliam")
        self.assertEqual(nomeCompleto2, "Peer Maximilliam Werner Kaus")




unittest.main(argv=[''], exit=False )














































