import vida
import unittest

class TestVida(unittest.TestCase):

    def test_iniciar_vida(self):
        vida.iniciar_vida()

        v = vida.vida

        self.assertEqual(30, v)

    def test_reduzir_vida(self):
        vida.vida = 10

        vida.reduzir_vida()

        self.assertEqual(9, vida.vida)

    def test_get_vida(self):
        vida.iniciar_vida()

        v = vida.get_vida()

        self.assertEqual(30, v)

    def test_set_vida(self):
        vida.set_vida(15)

        v = vida.get_vida()

        self.assertEqual(15, v)
        


if __name__ == '__main__':
    unittest.main(exit=False)
