import wave
import unittest

class TestWave(unittest.TestCase):

    def setUp(self):
        wave.remover_waves()
        wave.zerar_turn()

    def test_criar_wave(self):
        wave.criar_wave()

        self.assertEqual(1, len(wave.waves))
        

    def test_criar_duas_wave(self):
        wave.criar_wave()
        wave.criar_wave()

        self.assertEqual(2, len(wave.waves))
        self.assertEqual(2, wave.turn)


    def test_definir_wave(self):
        wave.criar_wave()
        wave.definir_wave()

        self.assertEqual(10, len(wave.waves["nojinho"]))

    def test_definir_duas_wave(self):
        wave.criar_wave()
        wave.definir_wave()
        wave.criar_wave()
        wave.definir_wave()

        self.assertEqual(12, len(wave.waves["nojinho"]))


    def test_diminuir_wave(self):
        wave.criar_wave()
        wave.definir_wave()

        wave.diminuir_wave(2)

        self.assertEqual(9, len(wave.waves["nojinho"]))
        

    def test_get_wave(self):
        wave.criar_wave()
        wave.criar_wave()
        wave.definir_wave()
        
        w = wave.get_wave()

    def test_criar_varias_wave(self):
        for i in range(10):
            wave.criar_wave()

    def test_definir_varias_waves(self):
        for i in range(5):
            wave.criar_wave()

        

if __name__ == '__main__':
    unittest.main(exit=False)
