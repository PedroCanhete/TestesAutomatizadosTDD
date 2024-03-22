from ClassesLeilao import Usuario, Lance, Leilao
from unittest import TestCase


class TestLeilao(TestCase):
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
        

    def teste_nao_deve_permitir_propor_lance_ordem_descrecente(self):
        with self.assertRaises(ValueError):
            bibi = Usuario('Bibi')
            lance_bibi = Lance(bibi, 150)
        
            self.leilao.propoe(lance_bibi)
            self.leilao.propoe(self.lance_pedro)


    def teste_retorno_maior_menor_valor_lance_unico(self):
        self.leilao.propoe(self.lance_pedro)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(100.0, self.leilao.maior_lance)

    def teste_retorno_maior_menor_valor_lances_multiplos(self):
        bibi = Usuario('Bibi')
        lance_bibi = Lance(bibi, 150)
        juanito_jones = Usuario('juanito')
        lance_juanito_jones = Lance(juanito_jones, 200.0)

        self.leilao.propoe(self.lance_pedro)
        self.leilao.propoe(lance_bibi)
        self.leilao.propoe(lance_juanito_jones)
        
        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_deve_permitir_propor_lance_caso_leilao_vazio(self):
        self.leilao.propoe(self.lance_pedro)
        quantidade_lances_recebidos = (len(self.leilao.lances))
        self.assertEqual(1, quantidade_lances_recebidos)
        
    def test_deve_permitir_propor_lance_caso_ultimo_lance_usuario_diferente(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 200)

        self.leilao.propoe(self.lance_pedro)
        self.leilao.propoe(lance_do_yuri)

        quantidade_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(2, quantidade_lances_recebidos)


    def teste_nao_permite_propor_lance_caso_mesma_pessoa(self):
        lance_pedro_novo = Lance(self.pedro, 200)
        with self.assertRaises(ValueError):
            #esse assertRaises é o método de teste em que o meu teste espera o ValueError, no caso, ele dará erro pois estou tentando dar 2 lances com o mesmo usuário
            self.leilao.propoe(self.lance_pedro)
            self.leilao.propoe(lance_pedro_novo)
