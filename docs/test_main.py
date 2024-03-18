
import main

def test_adivinhar_numero():
    numero_secreto = main.adivinhar_numero()
    assert 1 <= numero_secreto <= 100
    

def test_fazer_palpite(monkeypatch):
    jogador = {"nome": "Computador"}
    monkeypatch.setattr('builtins.input', lambda x: "50")
    assert main.fazer_palpite(jogador) in range(1, 101)   


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

#não está passando pq tem que tratar caso entre com número negativo
def test_printar_tentativas(capsys):
    jogador_computador = {"nome": "Computador", "palpites_computador": [1, 2, 3]}
    jogador_humano = {"nome": "Humano", "palpites_humano": [4, 5, 6]}

    main.printar_tentativas(jogador_computador)
    captured = capsys.readouterr()
    assert captured.out == "As tentativas do computador foram: 1 , 2 , 3"

   
    main.printar_tentativas(jogador_humano)
    captured = capsys.readouterr()
    assert captured.out == "Suas tentativas foram: 4 , 5 , 6"


def test_troca_jogadores():
    assert main.troca_jogadores(1) == 0
    assert main.troca_jogadores(0) == 1
    

def test_resetar_palpites():
    jogador1 = {"palpites_computador": [1, 2, 3], "palpites_humano": [4, 5, 6]}
    jogador2 = {"palpites_computador": [7, 8, 9], "palpites_humano": [10, 11, 12]}
    
    jogadores = [jogador1, jogador2]
    
    main.resetar_palpites(jogadores)
    
    assert jogador1["palpites_computador"] == []
    assert jogador1["palpites_humano"] == []
    


