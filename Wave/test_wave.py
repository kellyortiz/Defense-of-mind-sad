import wave
import unittest

class TestWave(unittest.TestCase):

    def setUp(self):
        wave.remover_waves()

    def test_criar_wave(self):
        wave.criar_wave()

        self.assertEqual(1, len(wave.waves))

    def test_definir_wave(self):
        wave.criar_wave()
        wave.definir_wave("tristeza")

        self.assertEqual(10, len(wave.waves["tristeza"]))

    def test_diminuir_wave(self):
        wave.criar_wave()
        wave.definir_wave("tristeza")

        wave.diminuir_wave(2)

        self.assertEqual(9, len(wave.waves["tristeza"]))
        

    def test_get_wave(self):
        wave.criar_wave()
        wave.definir_wave("tristeza")

        w = wave.get_wave("tristeza", 2)

        self.assertEqual(5, w["hp_total"])
        self.assertEqual(5, w["hp_atual"])
        self.assertEqual(3, w["velocidade_padrao"])
        self.assertEqual(3, w["velocidade_atual"])
        

if __name__ == '__main__':
    unittest.main(exit=False)
