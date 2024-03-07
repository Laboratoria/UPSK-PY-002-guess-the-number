import random

   
# função para sortear um número aleatório 
def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    return numero_secreto

# boas vindas ao jogo
print("Bem-vindo ao jogo de adivinhar o número!")
# perguntar o nome do jogador humano
nome_jogador = input("Qual é o seu nome? ")

# indicar início do jogo    
print("Vamos começar!")

# definição de jogadores
jogador = [ 
            {
                "nome": "Computador",
                "palpites_computador": []
                },

            {
                "nome": nome_jogador,
                "palpites_humano": []
                }
            ]

# função para fazer um palpite
def fazer_palpite(jogador,palpite):
    if jogador["nome"] == "Computador":
        palpite = random.randint(1, 100)
        print(f'{jogador["nome"]} palpitou {palpite}')
    else:
        palpite = int(input(f'{jogador["nome"]}, faça seu palpite: '))

#armazenar os palpites no array palpite de cada jogador
def armazenar_palpite(jogador, palpite):
    if jogador["nome"] == "Computador":
        jogador["palpites_computador"].append(palpite)
    else:
        jogador["palpites_humano"].append(palpite)
        
#função para analisar o palpite e printar se foi alto ou baixo        
def analisar_palpite(numero_secreto, palpite): 
    if palpite > numero_secreto: 
        print("O palpite foi maior que o número sorteado" ) 
    elif palpite < numero_secreto: 
        print("O palpite foi menor que o número sorteado")  
    else: 
        print("Parabéns! Você acertou o número sorteado") 
        


#loop para alternar entre jogadas do humano e computador    
numero_secreto = adivinhar_numero()
jogador = jogador[1]
while True:
    palpite = fazer_palpite(jogador, 0)  
    armazenar_palpite(jogador, palpite)
    analisar_palpite(jogador, 0)
    
    if palpite == numero_secreto:
        break 
    
    jogador = jogador[0]