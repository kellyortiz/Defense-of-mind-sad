import nojinho
import unittest
import pygame


class Testnojinho(unittest.TestCase):

    def test_criar_nojinho(self):
        b = nojinho.criar_nojinho(1)
        pygame.init()
        screen = pygame.display.set_mode((800, 650), 0, 0)
        img = pygame.image.load(b["img"]).convert_alpha()
        
        screen.blit(img, (b["x"], b["y"]))
        
        self.assertEqual(5, b["hp_total"])
        self.assertEqual(5, b["hp_atual"])
        self.assertEqual(3, b["velocidade_padrao"])
        self.assertEqual(3, b["velocidade_atual"])
        

        pygame.display.update()

    def test_iniciar_hp(self):
        nojinho.iniciar_hp()

        b = nojinho.hp

        self.assertEqual(5, b)

    def test_iniciar_velocidade(self):
        nojinho.iniciar_velocidade()

        v = nojinho.velocidade

        self.assertEqual(3, v)

    def test_definir_hp(self):
        nojinho.definir_hp(2)

        hp = nojinho.hp

        self.assertEqual(7, hp)

    def test_get_hp(self):
        hp = nojinho.get_hp()
        h = nojinho.hp

        self.assertEqual(hp, h)

    def test_set_hp(self):
        nojinho.set_hp(10)

        hp = nojinho.hp

        self.assertEqual(10, hp)

    def test_diminuir_hp(self):
        hp = 10
        hp = nojinho.diminuir_hp(2, hp)

        self.assertEqual(8, hp)

        

if __name__ == '__main__':
    unittest.main(exit=False)
