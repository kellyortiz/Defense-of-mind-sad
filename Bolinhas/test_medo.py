import medo
import unittest
import pygame

class Testmedo(unittest.TestCase):

    def test_criar_medo(self):
        b = medo.criar_medo(1)
        pygame.init()
        screen = pygame.display.set_mode((800, 650), 0, 0)
        img = pygame.image.load(b["img"]).convert_alpha()
        
        screen.blit(img, (b["x"], b["y"]))

        pygame.display.update()

        self.assertEqual(5, b["hp_total"])
        self.assertEqual(5, b["hp_atual"])
        self.assertEqual(3, b["velocidade_padrao"])
        self.assertEqual(3, b["velocidade_atual"])

    def test_iniciar_hp(self):
        medo.iniciar_hp()

        b = medo.hp

        self.assertEqual(5, b)

    def test_iniciar_velocidade(self):
        medo.iniciar_velocidade()

        v = medo.velocidade

        self.assertEqual(3, v)

    def test_definir_hp(self):
        medo.definir_hp(2)

        hp = medo.hp

        self.assertEqual(7, hp)

    def test_get_hp(self):
        hp = medo.get_hp()
        h = medo.hp

        self.assertEqual(hp, h)

    def test_set_hp(self):
        medo.set_hp(10)

        hp = medo.hp

        self.assertEqual(10, hp)

    def test_diminuir_hp(self):
        hp = 10
        hp = medo.diminuir_hp(2, hp)

        self.assertEqual(8, hp)

        

if __name__ == '__main__':
    unittest.main(exit=False)
