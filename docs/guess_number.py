"""Este é o programa principal"""

import main


# boas vindas ao jogo
print("Bem-vindo ao jogo de adivinhar o número!")
# perguntar o nome do jogador humano
nome_jogador = input("Qual é o seu nome? ")

# indicar início do jogo
print("Vamos começar!Tente advinhar um número entre 1 e 100")

# definição de jogadores
adversarios = [
    {
        "nome": "Computador",
                "palpites_computador": []
    },

    {
        "nome": nome_jogador,
        "palpites_humano": []
    }
]

main.roda_jogo(adversarios)
