"""Aqui estão os testes de cada função do main.py"""

from unittest import mock
import main



# ok
def test_adivinhar_numero():
    """Teste para ver se o número sorteado está entre 1 e 100"""
    numero_secreto = main.adivinhar_numero()
    assert isinstance(numero_secreto, int)
    assert numero_secreto >= 1
    assert numero_secreto <= 100


def test_fazer_palpite_computador():
    """Teste para ver se o palpite feito pelo jogador computador está entre 1 e 100"""
    jogador = {"nome": "Computador"}
    palpite_computador = main.fazer_palpite(jogador)
    assert isinstance(palpite_computador, int)
    assert palpite_computador >= 1 and palpite_computador <= 100

def test_fazer_palpite_humano():
    """Teste para ver se o palpite feito pelo jogador humano está entre 1 e 100"""
    with mock.patch("builtins.input", mock.Mock(return_value="5")):
        jogador = {"nome": "Antonio"}
        palpite_humano = main.fazer_palpite(jogador)
        assert isinstance(palpite_humano, int)
        assert palpite_humano >= 1 and palpite_humano <= 100


def test_fazer_palpite_invalid():
    """Teste para analisar se quando o palpite feito for invalido, se está retornando uma mensagem
    de erro """
    with mock.patch("builtins.input", mock.Mock(return_value="-8")):
        jogador = {"nome": "Maila"}
        palpite_humano = main.fazer_palpite(jogador)
        assert isinstance(palpite_humano, int)



# ok
def test_armazenar_palpite():
    """Teste para ver se está sendo armazenado os palpites no array correto"""
    jogador_computador = {
        "nome": "Computador",
        "palpites_computador": []
    }
    jogador_humano = {
        "nome": "Humano",
        "palpites_humano": []
    }

    palpite1 = 5
    palpite2 = 8

    main.armazenar_palpite(jogador_computador, palpite1)
    main.armazenar_palpite(jogador_humano, palpite2)

    assert jogador_computador["palpites_computador"] == [5]
    assert jogador_humano["palpites_humano"] == [8]

    main.armazenar_palpite(jogador_computador, 10)
    main.armazenar_palpite(jogador_humano, 3)

    assert jogador_computador["palpites_computador"] == [5, 10]
    assert jogador_humano["palpites_humano"] == [8, 3]

# não está passando


def test_analisar_palpite():
    """Teste para analisar se o palpite foi naior, menor ou igual ao sorteado"""
    numero_secreto = 50
    palpite = 40
    assert main.analisar_palpite(
        numero_secreto, palpite) == "O palpite foi menor que o número sorteado"

    numero_secreto = 40
    palpite = 50
    assert main.analisar_palpite(
        numero_secreto, palpite) == "O palpite foi maior que o número sorteado"

    numero_secreto = 50
    palpite = 50
    assert main.analisar_palpite(
        numero_secreto, palpite) == "Parabéns! Você acertou o número sorteado"


# não está passando pq tem que tratar caso entre com número negativo
def test_printar_tentativas(capsys):
    """Teste para ver se está sendo printado na tela os números corretos que o vencedor palpitou"""
    jogador_computador = {
        "nome": "Computador",
        "palpites_computador": [1, 2, 3]
    }

    jogador_humano = {
        "nome": "Jogador",
        "palpites_humano": [4, 5, 6]
    }

    main.printar_tentativas(jogador_computador)
    captured = capsys.readouterr()
    assert captured.out == "As tentativas do computador foram: 1 , 2 , 3"

    main.printar_tentativas(jogador_humano)
    captured = capsys.readouterr()
    assert captured.out == "Suas tentativas foram: 4 , 5 , 6"

# ok


def test_troca_jogadores():
    """Testa se está trocando corretamente de jogadores a cada jogada """
    assert main.troca_jogadores(1) == 0
    assert main.troca_jogadores(0) == 1

# ok


def test_resetar_palpites():
    """Testa se a função está zerando o array de palpites quando solicitado um novo jogo"""
    jogador1 = {"palpites_computador": [1, 2, 3], "palpites_humano": [4, 5, 6]}
    jogador2 = {"palpites_computador": [
        7, 8, 9], "palpites_humano": [10, 11, 12]}

    jogadores = [jogador1, jogador2]

    main.resetar_palpites(jogadores)

    assert not jogador1["palpites_computador"]
    assert not jogador1["palpites_humano"]
    