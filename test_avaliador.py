from ClassesLeilao import Usuario, Lance, Leilao
from unittest import TestCase


class TestAvaliador(TestCase):
    def setUp(self):
        self.pedro = Usuario('Pedro')
        self.lance_pedro = Lance(self.pedro, 100)
        self.leilao = Leilao('Carro 0Km')

    
    
    def teste_retorno_maior_menor_valor_lances_adicionados_ordem_crescente(self):
        bibi = Usuario('Bibi')
        lance_bibi = Lance(bibi, 150)

        self.leilao.propoe(self.lance_pedro)
        self.leilao.propoe(lance_bibi)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
        

    def teste_retorno_maior_menor_valor_lances_adicionados_ordem_decrescente(self):
        bibi = Usuario('Bibi')
        lance_bibi = Lance(bibi, 150)
        
        self.leilao.propoe(lance_bibi)
        self.leilao.propoe(self.lance_pedro)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def teste_retorno_maior_menor_valor_lance_unico(self):
        self.leilao.propoe(self.lance_pedro)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(100.0, self.leilao.maior_lance)

    def teste_retorno_maior_menor_valor_lances_multiplos(self):
        bibi = Usuario('Bibi')
        lance_bibi = Lance(bibi, 150)
        juanito_jones = Usuario('juanito')
        lance_juanito_jones = Lance(juanito_jones, 200.0)

        self.leilao.propoe(lance_bibi)
        self.leilao.propoe(self.lance_pedro)
        self.leilao.propoe(lance_juanito_jones)
        
        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

