import raiva
import unittest
import pygame

class Testraiva(unittest.TestCase):

    def test_criar_raiva(self):
        b = raiva.criar_raiva(1)
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
        raiva.iniciar_hp()

        b = raiva.hp

        self.assertEqual(5, b)

    def test_iniciar_velocidade(self):
        raiva.iniciar_velocidade()

        v = raiva.velocidade

        self.assertEqual(3, v)

    def test_definir_hp(self):
        raiva.definir_hp(2)

        hp = raiva.hp

        self.assertEqual(7, hp)

    def test_get_hp(self):
        hp = raiva.get_hp()
        h = raiva.hp

        self.assertEqual(hp, h)

    def test_set_hp(self):
        raiva.set_hp(10)

        hp = raiva.hp

        self.assertEqual(10, hp)

    def test_diminuir_hp(self):
        hp = 10
        hp = raiva.diminuir_hp(2, hp)

        self.assertEqual(8, hp)

        

if __name__ == '__main__':
    unittest.main(exit=False)
