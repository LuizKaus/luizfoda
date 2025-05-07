import unittest
from Aula14textes import Prova

class ProvaTest(unittest.TestCase):

    def test_armazenaQuestao(self):
        questao = "Quanto é 3 + peixe"
        p = Prova()
        p.armazenaQuestoesRespostas(questao, "")
        self.assertIn("Quanto é 3 + peixe", p.questoes)

unittest.main(argv=[''], exit = False)


















