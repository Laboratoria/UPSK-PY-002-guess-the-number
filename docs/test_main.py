
import main
from unittest import mock


#ok
def test_adivinhar_numero():
    numero_secreto = main.adivinhar_numero()
    assert isinstance(numero_secreto, int)
    assert numero_secreto >= 1
    assert numero_secreto <= 100
    
def test_fazer_palpite():
    jogador = {"nome": "Computador"}
    palpite_computador = main.fazer_palpite(jogador)
    assert isinstance(palpite_computador, int)
    assert palpite_computador >= 1 and palpite_computador <= 100
    
    with mock.patch("builtins.input", mock.Mock(return_value="5")):
        jogador = {"nome": "Antonio"}
        palpite_humano = main.fazer_palpite(jogador)
        assert isinstance(palpite_humano, int)
        assert palpite_humano >= 1 and palpite_humano <= 100
    
"""def test_fazer_palpite_invalid():
    with mock.patch("builtins.input", mock.Mock(return_value="-8")):
        jogador = {"nome": "Maila"}
        palpite_humano = main.fazer_palpite(jogador)
        assert isinstance(palpite_humano, int)
        assert 
"""                
   
    
#ok
def test_armazenar_palpite():
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
    
#não está passando
def test_analisar_palpite():
    numero_secreto = 50
    palpite = 40
    assert main.analisar_palpite(numero_secreto, palpite) == "O palpite foi menor que o número sorteado"

    numero_secreto = 40
    palpite = 50
    assert main.analisar_palpite(numero_secreto, palpite) == "O palpite foi maior que o número sorteado"
    
    numero_secreto = 50
    palpite = 50
    assert main.analisar_palpite(numero_secreto, palpite) == "Parabéns! Você acertou o número sorteado"
    
    
#não está passando pq tem que tratar caso entre com número negativo
def test_printar_tentativas(capsys):
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

#ok
def test_troca_jogadores():
    assert main.troca_jogadores(1) == 0
    assert main.troca_jogadores(0) == 1
    
#ok
def test_resetar_palpites():
    jogador1 = {"palpites_computador": [1, 2, 3], "palpites_humano": [4, 5, 6]}
    jogador2 = {"palpites_computador": [7, 8, 9], "palpites_humano": [10, 11, 12]}
    
    jogadores = [jogador1, jogador2]
    
    main.resetar_palpites(jogadores)
    
    assert jogador1["palpites_computador"] == []
    assert jogador1["palpites_humano"] == []
    
'''
@patch("builtins.print", side_effect=print)
def test_roda_jogo(patched_print):
    jogadores = ["Jogador1", "Jogador2"]  # jogadores para teste
    jogadores_cycle = itertools.cycle(jogadores)

    with patch("main.adivinhar_numero", return_value=10):
        with patch("main.fazer_palpite") as mocked_fazer_palpite:
            mocked_fazer_palpite.return_value = 10

            main.roda_jogo(jogadores_cycle)

    assert patched_print.call_count == 3
    assert patched_print.call_args_list == [
        (('Visualizando tentativas - Jogador1',), {}),
        (('Visualizando tentativas - Jogador2',), {}),
        (('Visualizando tentativas - Jogador1',), {}),
    ]
'''
