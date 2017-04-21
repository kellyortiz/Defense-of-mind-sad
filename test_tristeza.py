import tristeza
import unittest

class TestTristeza(unittest.TestCase):

    def test_criar_tristeza(self):
        b = tristeza.criar_tristeza(1)

        self.assertEqual(5, b["hp_total"])
        self.assertEqual(5, b["hp_atual"])
        self.assertEqual(3, b["velocidade_padrao"])
        self.assertEqual(3, b["velocidade_atual"])

    def test_iniciar_hp(self):
        tristeza.iniciar_hp()

        b = tristeza.hp

        self.assertEqual(5, b)

    def test_iniciar_velocidade(self):
        tristeza.iniciar_velocidade()

        v = tristeza.velocidade

        self.assertEqual(3, v)

    def test_definir_hp(self):
        tristeza.definir_hp(2)

        hp = tristeza.hp

        self.assertEqual(7, hp)

    def test_get_hp(self):
        hp = tristeza.get_hp()
        h = tristeza.hp

        self.assertEqual(hp, h)

    def test_set_hp(self):
        tristeza.set_hp(10)

        hp = tristeza.hp

        self.assertEqual(10, hp)

    def test_diminuir_hp(self):
        hp = 10
        hp = tristeza.diminuir_hp(2, hp)

        self.assertEqual(8, hp)

        

if __name__ == '__main__':
    unittest.main(exit=False)
