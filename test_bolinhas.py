import bolinhas
import unittest

class TestBolinhas(unittest.TestCase):

    def test_criar_bolinha(self):
        b = bolinhas.criar_bolinha(5, 3)

        self.assertEqual(5, b["hp_total"])
        self.assertEqual(5, b["hp_atual"])
        self.assertEqual(3, b["velocidade_padrao"])
        self.assertEqual(3, b["velocidade_atual"])

    def test_diminuir_hp(self):
        resultado = bolinhas.diminuir_hp(1, 5)
        self.assertEqual(4, resultado)

if __name__ == '__main__':
    unittest.main(exit=False)
