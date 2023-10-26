import unittest

from src.crianca import Crianca


class CriancaTest(unittest.TestCase):

    def testInicializandoCrianca(self):
        crianca = Crianca("Dora", 6)
        self.assertEqual(6, crianca.getIdade(),
                     "Ao inicializar uma crianca ela deve ter a mesma idade que foi passada na inicialização")
        self.assertEqual("Dora", crianca.getNome(),
                     "Ao inicializar uma crianca ela deve ter o mesmo nome que foi passada na inicialização")

if __name__ == '__main__':
    unittest.main()