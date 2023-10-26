import unittest

from src.crianca import Crianca
from src.pula_pula import PulaPula

class PulaPulaTest(unittest.TestCase):

    def testInicializacao(self):
        pulaPula = PulaPula(5)
        self.assertEqual(5, pulaPula.getLimiteMax(),
                         "Ao inicializar um pula-pula ela deve vir com o limite exato ao que foi passado na inicialização.")
        self.assertEqual(0, pulaPula.getCaixa(),
                         "Ao inicializar um pula-pula ela deve vir com o caixa zerado.")
        self.assertEqual([], pulaPula.getFilaDeEspera(),
                        "Ao inicializar o pula-pula não deve haver ninguém na fila de espera.")
        self.assertEqual([], pulaPula.getCriancasPulando(),
                        "Ao inicializar o pula-pula não deve haver ninguém dentro do pula-pula.")

    def testPrimeiroDaFila(self):
        pulaPula = PulaPula(5)
        pulaPula.entrarNaFila(Crianca("maria", 6))
        crianca = Crianca("ana", 7)
        pulaPula.entrarNaFila(crianca)
        self.assertEqual(crianca, pulaPula.getFilaDeEspera()[len(pulaPula.getFilaDeEspera()) - 1],
                         "Quando uma crianca chega na fila ela deve ser insirida na última posição.")

    def testEntrarNoPulaPulaSemNinguemNaFila(self):
        pulaPula = PulaPula(5)
        self.assertFalse(pulaPula.entrar(),
                         "Não deve ser possível entrar no pula-pula se não estiver ninguém na fila.")

    def testAdicionarDuasCriancasComNomeIgual(self):
        pulaPula = PulaPula(1)
        self.assertTrue(pulaPula.entrarNaFila(Crianca("pedro", 7)),
                        "Deve ser possível entrar no pula-pula se não houver nenhuma restrição")
        self.assertFalse(pulaPula.entrarNaFila(Crianca("pedro", 3)),
                         "Não deve ser possível uma crianca entrar na fila se já existe outra crianca na fila ou no pula-pula")

    def testEntrarNoPulaPulaNoLimiteMaximo(self):
        pulaPula = PulaPula(1)
        pulaPula.entrarNaFila(Crianca("maria", 6))
        pulaPula.entrarNaFila(Crianca("ana", 3))
        self.assertTrue(pulaPula.entrar(),
                        "Se o limite do pula-pula não foi alcançado, deve ser possível entrar no pula-pula.")
        self.assertFalse(pulaPula.entrar(),
                         "Não deve ser possível entrar no pula-pula se o limite máximo ja foi alcançado.")

    def testPrimeiroDaFilaEntraNoPulaPula(self):
        pulaPula = PulaPula(1)
        crianca = Crianca("maria", 6)
        pulaPula.entrarNaFila(crianca)
        pulaPula.entrarNaFila(Crianca("ana", 3))
        self.assertTrue(pulaPula.entrar(),
                        "Deve ser possível entrar no pula-pula se não houver nenhuma restrição")
        self.assertEqual(crianca, pulaPula.getCriancasPulando()[0],
                         "Quando uma crianca entra no pula-pula ela tem necessiaremente tem quer ser a primeira da fila.")

    def testEntraNoPulaPulaSaiDaFila(self):
        pulaPula = PulaPula(1)
        pulaPula.entrarNaFila(Crianca("ana", 3))
        self.assertTrue(pulaPula.entrar(),
                        "Se o limite do pula-pula não foi alcançado, deve ser possível entrar no pula-pula.")
        self.assertEqual(0, len(pulaPula.getFilaDeEspera()),
                         "Quando uma crianca entra no pula-pula, ela automaticamente sai da fila de espera.")

    def testSairDoPulaPulaSemNinguemNoPulaPula(self):
        pulaPula = PulaPula(1)
        self.assertFalse(pulaPula.sair(),
                         "Não deve ser possível sair do pula-pula se não nenhuma crianca dentro do pula-pula")

    def testSairDoPulaPulaComSucesso(self):
        pulaPula = PulaPula(1)
        pulaPula.entrarNaFila(Crianca("ana", 3))
        self.assertTrue(pulaPula.entrar(),
                        "Se o limite do pula-pula não foi alcançado, deve ser possível entrar no pula-pula.")
        self.assertTrue(pulaPula.sair(),
                        "Deve ser possível sair se houver pelo menos uma crianca dentro do pula-pula")

    def testPrimeiroQueEntraPrimeiroQueSai(self):
        pulaPula = PulaPula(1)
        crianca = Crianca("maria", 6)
        pulaPula.entrarNaFila(crianca)
        pulaPula.entrarNaFila(Crianca("ana", 3))
        self.assertTrue(pulaPula.entrar(),
                        "Se o limite do pula-pula não foi alcançado, deve ser possível entrar no pula-pula.")
        pulaPula.entrar();
        self.assertTrue(pulaPula.sair(),
                        "Se houve crianca no pula-pula, deve ser possível a crianca sair do pula-pula.")
        self.assertEqual(crianca, pulaPula.getFilaDeEspera()[len(pulaPula.getFilaDeEspera()) - 1],
                         "Quando uma crianca sai do pula-pula, ela automatica entra no fim da fila de espera")

    def testEntrandoNoPulaPulaEAdicionandoSaldoNaConta(self):
        pulaPula = PulaPula(1)

        crianca = Crianca("maria", 6)
        pulaPula.entrarNaFila(crianca)
        self.assertTrue(pulaPula.entrar(),
                        "Se o limite do pula-pula não foi alcançado, deve ser possível entrar no pula-pula.")
        self.assertTrue(pulaPula.sair(),
                        "Se houve crianca no pula-pula, deve ser possível a crianca sair do pula-pula.")
        pulaPula.entrar()
        self.assertEqual(5.00, pulaPula.getConta(crianca.getNome()),
                         "Tpda vez que uma crianca entra no pula-pula é acrescido na sua conta o valor de R$ 2,50.")

    def testPaipaiChegouENaoTinhaNinguem(self):
        pulaPula = PulaPula(1)
        self.assertFalse(pulaPula.papaiChegou("Pedro"),
                         "Não deve ser possível chamar uma crianca se não ninguem na fila ou no pula-pula")

    def testPapaiChamouPorUmNomeErrado(self):
        pulaPula = PulaPula(1)
        pulaPula.entrarNaFila(Crianca("Eduardo", 7))
        self.assertFalse(pulaPula.papaiChegou("Diego"),
                         "Não deve ser possível encontrar uma crianca com o nome diferente daquelas que estão na fila ou pula-pula.")

    def testPapaiChamouCriancaDaFila(self):
        pulaPula = PulaPula(1)
        pulaPula.entrarNaFila(Crianca("Eduardo", 7))
        self.assertTrue(pulaPula.papaiChegou("Eduardo"),
                        "Deve ser possível encontrar uma crianca com o nome certo quando ela está na fila")

    def testPaipaiChamouCriancaDoPulaPula(self):
        pulaPula = PulaPula(1)
        pulaPula.entrarNaFila(Crianca("Luiz", 8))
        pulaPula.entrar()
        self.assertTrue(pulaPula.papaiChegou("Luiz"),
                        "Deve ser possível encontrar uma crianca com o nome certo quando ela está no pula-pula")

    def testPaipaiChamouCriancaPulandoEPagouAConta(self):
        pulaPula = PulaPula(1)
        pulaPula.entrarNaFila(Crianca("Eduardo", 7))
        self.assertTrue(pulaPula.entrar(),
                        "Se o limite do pula-pula não foi alcançado, deve ser possível entrar no pula-pula.")
        self.assertTrue(pulaPula.sair(),
                        "Se houver crianca no pula-pula, deve ser possível a crianca sair do pula-pula.")
        pulaPula.entrar()
        pulaPula.papaiChegou("Eduardo")
        self.assertEqual(5.00, pulaPula.getCaixa(),
                         "Quando um crianca vai embora, o seu pai deve pagar a conta e o dinheiro vai direto para o caixa.")

    def testPaipaiChamouCriancaNaFilaEPagouAConta(self):
        pulaPula = PulaPula(1)
        pulaPula.entrarNaFila(Crianca("Eduardo", 7))
        self.assertTrue(pulaPula.entrar(),
                        "Se o limite do pula-pula não foi alcançado, deve ser possível entrar no pula-pula.")
        self.assertTrue(pulaPula.sair(),
                        "Se houver crianca no pula-pula, deve ser possível a crianca sair do pula-pula.")
        pulaPula.papaiChegou("Eduardo")
        self.assertEqual(2.50, pulaPula.getCaixa(),
                         "Quando um crianca vai embora, o seu pai deve pagar a conta e o dinheiro vai direto para o caixa.")

    def testFecharPulaPula(self):
        pulaPula = PulaPula(2)
        pulaPula.entrarNaFila(Crianca("Eduardo", 7))
        pulaPula.entrar()
        pulaPula.entrarNaFila(Crianca("Luiz", 8))
        self.assertTrue(pulaPula.fechar(),
                         "Ao fechar todas as criancas que entraram no pula-pula devem pagar as contas.")
        self.assertEqual(0, len(pulaPula.getFilaDeEspera()),
                         "Ao fechar o pula-pula todas as crianças são retiradas da fila.")
        self.assertEqual(0, len(pulaPula.getCriancasPulando()),
                         "Ao fechar o pula-pula todas as crianças são retiradas da fila.")
        self.assertIsNone(pulaPula.getConta("Eduardo"),
                          "Ao fechar o pula-pula, todas as contas de todas as crianças são excluídas")

    def testPegarContaQueNaoExiste(self):
        pulaPula = PulaPula(2)
        pulaPula.entrarNaFila(Crianca("Eduardo", 7))
        self.assertIsNone(pulaPula.getConta("Eduardo"),
                          "Não deve ser possível pegar a conta de uma criança que não entrou no pula-pula.")

if __name__ == '__main__':
    unittest.main()