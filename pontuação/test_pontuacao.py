import pontuacao
import unittest

class TestPontuacao(unittest.TestCase):

      def test_iniciar_pontuacao(self):
        pontuacao.iniciar_pontuacao()
        
        p = pontuacao.pontuacao
        
        self.assertEqual(0, p)

      def test_aumentar_pontuacao(self):
        pontuacao.pontuacao = 10
        
        pontuacao.aumentar_pontuacao(8)
        
        self.assertEqual(18, pontuacao.ponto)

      def test_get_pontuacao(self):
        pontuacao.iniciar_pontuacao()

        p = pontuacao.get_pontuacao()

        self.assertEqual(0, p)

      def test_set_pontuacao(self):
        pontuacao.set_pontuacao(15)

        p = pontuacao.get_pontuacao()

        self.assertEqual(15, p)
        


if __name__ == '__main__':
    unittest.main(exit=False)
