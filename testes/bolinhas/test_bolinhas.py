import bolinhas
import unittest
import pygame

class TestBolinhas(unittest.TestCase):

    def test_criar_bolinha(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 650), 0, 0)
        img = pygame.image.load('fear.png').convert_alpha()
        b = bolinhas.criar_bolinha(5, 3, img)

        screen.blit(b["img"], (b["x"], b["y"]))
        self.assertEqual(5, b["hp_total"])
        self.assertEqual(5, b["hp_atual"])
        self.assertEqual(3, b["velocidade_padrao"])
        self.assertEqual(3, b["velocidade_atual"])
        pygame.display.update()

    def test_diminuir_hp(self):
        resultado = bolinhas.diminuir_hp(1, 5)
        self.assertEqual(4, resultado)

if __name__ == '__main__':
    unittest.main(exit=False)
