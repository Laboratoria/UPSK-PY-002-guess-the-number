"""Este local é onde armazenamos as funções para serem chamadas no programa principal"""

import random


def adivinhar_numero():
    """Esta função fará uma escolha aleatória de um número
    a = random.randint(1,100)
    Returns: a """
    numero_secreto = random.randint(1, 100)
    return numero_secreto



def fazer_palpite(jogador):
    """Função que faz o palpite tanto do computador como do jogador"""
    palpite = 0
    if jogador["nome"] == "Computador":
        palpite = random.randint(1, 100)
        print(f'{jogador["nome"]} palpitou {palpite}')
    else:
        while True:
            try:
                palpite = int(input(f'{jogador["nome"]}, faça seu palpite: '))
                if palpite >= 1 and palpite <= 100:
                    break
                else:
                    print("Apenas números entre 1 e 100.")
            except ValueError:
                print("Apenas números entre 1 e 100.")
    return palpite


def armazenar_palpite(jogador, palpite):
    """Armazena os palpites no array de cada jogador"""
    if jogador["nome"] == "Computador":
        jogador["palpites_computador"].append(palpite)
    else:
        jogador["palpites_humano"].append(palpite)



def analisar_palpite(numero_secreto, palpite):
    """Função para analisar palpites e printar se foi alto, baixo ou correto"""
    if palpite > numero_secreto:
        print("O palpite foi maior que o número sorteado")
    elif palpite < numero_secreto:
        print("O palpite foi menor que o número sorteado")
    else:
        print("Parabéns! Você acertou o número sorteado")



def reiniciar_jogo(jogadores):
    """Função para reiniciar o jogo caso o jogador queira"""
    resetar_palpites(jogadores)
    resposta = input("Deseja reiniciar o jogo? (s/n): ")

    if resposta.lower() == 's':
        roda_jogo(jogadores)
    elif resposta.lower() == 'n':
        print("Fim de jogo!")
    else:
        print("Por favor, digite apenas 's' para sim ou 'n' para não:")
        reiniciar_jogo(jogadores)


def printar_tentativas(jogador):
    """Função para printar tentativas do vencedor"""
    if jogador["nome"] == "Computador":
        print(f"As tentativas do computador foram: \
            { ' , '.join(map(str, jogador['palpites_computador']))}")
    else:
        print(f"Suas tentativas foram: { ' , '.join(map(str, jogador['palpites_humano']))}")


def troca_jogadores(beterraba):
    """Função para alternar os jogadores"""
    if beterraba == 1:
        beterraba = 0
    else:
        beterraba = 1
    return beterraba



def resetar_palpites(jogadores):
    """Função para resetar palpites para um novo jogo"""
    for jogador in jogadores:
        jogador["palpites_computador"] = []
        jogador["palpites_humano"] = []


def roda_jogo(jogadores):
    """Loop para alternar entre jogadas do humano e computador"""
    numero_secreto = adivinhar_numero()
    index = 1
    while True:
        jogador = jogadores[index]
        palpite = fazer_palpite(jogador)
        armazenar_palpite(jogador, palpite)
        analisar_palpite(numero_secreto, palpite)
        print('-=-'*20)

        if palpite == numero_secreto:
            printar_tentativas(jogador)
            print('-=-'*20)
            reiniciar_jogo(jogadores)
            break

        index = troca_jogadores(index)
