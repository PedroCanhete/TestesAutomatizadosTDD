from ClassesLeilao import Usuario, Lance, Leilao
from tests.excessoes import LanceInvalido
import pytest


@pytest.fixture
def pedro():
    return Usuario('Pepe Periculoso', 100)

@pytest.fixture
def leilao():
    return Leilao('Um Saco Balas Juquinhas')

def test_deve_subtrair_valor_carteira_do_usuario_ao_propor_lance(pedro, leilao):
    pedro.propoe_lance(leilao, 80)

    assert pedro.carteira == 20


def test_deve_permitir_propor_lance_quando_valor_eh_menor_que_carteira(pedro, leilao):
    pedro.propoe_lance(leilao, 10)

    assert pedro.carteira == 90

def test_deve_permiri_propor_lance_quando_valor_eh_igual_carteira(pedro, leilao):
    pedro.propoe_lance(leilao, 100)

    assert pedro.carteira == 0


def test_nao_deve_permitir_propor_quando_valor_maior_que_carteira(pedro, leilao):
    with pytest.raises(LanceInvalido):
        pedro.propoe_lance(leilao, 200)
